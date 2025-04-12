
# Obejct following robot

This project uses YOLOv8 (You Only Look Once version 8) for real-time Obejct detection and controls a robot's movement via MQTT. The system detects the Obejct in the camera feed and sends commands to the robot to move forward, left, right, or stop based on the detected Obejct's position. The robot movement is controlled via an L298N motor driver and a Raspberry Pi.


## Features

Real-time Obejct Detection: Using YOLOv8 to detect object in the camera feed.

Robot Movement Control: Commands like forward, left, right, and stop are sent via MQTT based on the detected Obejct's position.

MQTT Communication: MQTT is used to communicate between the computer running YOLOv8 and the Raspberry Pi controlling the motors.


## Hardware Requirement

Raspberry Pi 

Camera (Bluetooth webcam connected to the laptop)

L298N Motor Driver

DC motors

GPIO pins for motor control



## Software Requirement

Python 3

OpenCV (opencv library)

YOLOv8 model (ultralytics library)

MQTT client (paho-mqtt library)

Raspberry Pi GPIO library (RPi.GPIO)

## Setup (Laptop)

Run the following commands on the Laptop:

```bash
  pip install opencv-python
  pip install paho-mqtt
  pip install ultralytics
```
## Setup (Raspberry pi)

Run the following commands on the 
Raspberry pi:
 
 : RPi.GPIO Download
```bash
  sudo apt update
  pip install RPi.GPIO
  ```

: mqtt Download
```bash
  sudo apt update
  pip install paho-mqtt
  sudo apt install mosquitto mosquitto-clients
  ```

: mqtt Setup
```bash
  sudo systemctl enable mosquitto
  sudo systemctl start mosquitto
  ```



  
  
## Acknowledgements

  - [Ultrayltics](https://github.com/ultralytics/ultralytics)
  - [OpenCV](https://github.com/opencv/opencv)
  - [paho-mqtt](https://github.com/eclipse-paho/paho.mqtt.python)
 
