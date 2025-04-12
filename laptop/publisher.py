import cv2
import paho.mqtt.client as mqtt
from ultralytics import YOLO

# Load YOLOv8 
model = YOLO("yolov8n.pt")

# MQTT configuration
broker = "###.###.#.##"#Raspberry pi's ip address
topic = "robot/movement"

# Connect to MQTT broker
client = mqtt.Client()
client.connect(broker, 1883, 60)

# Minimum confidence
conf_thresh = 0.5

# Start video capture
cap = cv2.VideoCapture(1)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLO 
    results = model(frame)
    found = False

    for res in results:
        for box in res.boxes:
            conf = box.conf[0].item()
            cls = int(box.cls[0])

            # Check if detected object is a person and confidence is high
            if cls == 0 and conf >= conf_thresh:
                found = True
                x = box.xywh[0][0].item()

                # Decide movement direction based on horizontal position
                if x < frame.shape[1] // 3:
                    dir = "left"
                elif x > 2 * frame.shape[1] // 3:
                    dir = "right"
                else:
                    dir = "forward"

                client.publish(topic, dir)
                print(f"Person {conf:.2f}: {dir}")
                break

    # If no person detected, stop movement
    if not found:
        client.publish(topic, "stop")
        print("No person: stop")

    # Display detection result
    cv2.imshow("yolo", results[0].plot())
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup on exit
client.publish(topic, "stop")
cap.release()
cv2.destroyAllWindows()
client.disconnect()
