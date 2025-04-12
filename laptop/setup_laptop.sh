#!/bin/bash

echo " Updating package list..."
sudo apt update -y

echo " Installing pip3..."
sudo apt install -y python3-pip

echo " Installing OpenCV..."
pip3 install opencv-python

echo " Installing Ultralytics (YOLO)..."
pip3 install ultralytics

echo " Installing paho-mqtt..."
pip3 install paho-mqtt

echo " All Python libraries installed successfully on laptop!"
