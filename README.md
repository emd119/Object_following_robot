Obejct Detection and Object following robot:
This project uses YOLOv8 (You Only Look Once version 8) for real-time object detection and controls a robot's movement via MQTT. The system detects the object in the 
camera feed and sends commands to the robot to move forward, left, right, or stop based on the detected person's position. The robot movement is controlled via an L298N 
motor driver and a Raspberry Pi.

Features
Real-time Object Detection: Using YOLOv8 to detect people in the camera feed.

Robot Movement Control: Commands like forward, left, right, and stop are sent via MQTT based on the detected Object's position.

MQTT Communication: MQTT is used to communicate between the computer running YOLOv8 and the Raspberry Pi controlling the motors.

Components Needed
Hardware:

Raspberry Pi 3 or higher

Camera (a Blutooth camera connected to thelaptop)

L298N Motor Driver

DC motors

Software:

Python 3

OpenCV (opencv library)

YOLOv8 model (ultralytics library)

MQTT client (paho-mqtt library)

Raspberry Pi GPIO library (RPi.GPIO)
