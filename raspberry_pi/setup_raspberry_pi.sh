#!/bin/bash

echo "🔄 Updating system..."
sudo apt update -y && sudo apt upgrade -y

echo "🐍 Installing Python3 and pip..."
sudo apt install -y python3 python3-pip

echo "📦 Installing RPi.GPIO..."
sudo apt install -y python3-rpi.gpio

echo "📡 Installing Mosquitto broker and client..."
sudo apt install -y mosquitto mosquitto-clients

echo "🔌 Enabling Mosquitto service..."
sudo systemctl enable mosquitto
sudo systemctl start mosquitto

echo "🐍 Installing required Python libraries..."
pip3 install paho-mqtt

echo "✅ Setup complete!"
echo "➡️ Mosquitto MQTT broker is running"
