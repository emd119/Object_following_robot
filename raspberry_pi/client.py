import RPi.GPIO as gpio
import paho.mqtt.client as mqtt

# Motor pins
in1, in2 = 17, 18
in3, in4 = 22, 23
ena, enb = 24, 25

# Setup GPIO
gpio.setmode(gpio.BOARD)
gpio.setup([in1, in2, in3, in4, ena, enb], gpio.OUT)

# PWM setup
pwm_a = gpio.PWM(ena, 1000)
pwm_b = gpio.PWM(enb, 1000)
pwm_a.start(0)
pwm_b.start(0)

# MQTT settings
broker = "###.###.#.##"
topic = "robot/movement"

# Movement functions
def move_fwd():
    gpio.output(in1, gpio.HIGH)
    gpio.output(in2, gpio.LOW)
    gpio.output(in3, gpio.HIGH)
    gpio.output(in4, gpio.LOW)
    pwm_a.ChangeDutyCycle(70)
    pwm_b.ChangeDutyCycle(70)

def move_left():
    gpio.output(in1, gpio.LOW)
    gpio.output(in2, gpio.HIGH)
    gpio.output(in3, gpio.HIGH)
    gpio.output(in4, gpio.LOW)
    pwm_a.ChangeDutyCycle(50)
    pwm_b.ChangeDutyCycle(70)

def move_right():
    gpio.output(in1, gpio.HIGH)
    gpio.output(in2, gpio.LOW)
    gpio.output(in3, gpio.LOW)
    gpio.output(in4, gpio.HIGH)
    pwm_a.ChangeDutyCycle(70)
    pwm_b.ChangeDutyCycle(50)

def stop():
    gpio.output(in1, gpio.LOW)
    gpio.output(in2, gpio.LOW)
    gpio.output(in3, gpio.LOW)
    gpio.output(in4, gpio.LOW)
    pwm_a.ChangeDutyCycle(0)
    pwm_b.ChangeDutyCycle(0)

# Handle incoming MQTT messages
def on_msg(client, data, msg):
    cmd = msg.payload.decode()
    print(f"Received: {cmd}")

    if cmd == "forward":
        move_fwd()
    elif cmd == "left":
        move_left()
    elif cmd == "right":
        move_right()
    elif cmd == "stop":
        stop()

# MQTT setup
client = mqtt.Client()
client.on_message = on_msg
client.connect(broker, 1883, 60)
client.subscribe(topic)

print("Waiting for commands...")
client.loop_forever()
