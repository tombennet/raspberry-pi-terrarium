#!/usr/bin/python3

# lights-off.py - For Terrarium Controllers using Adafruit
# DHT sensors, Energenie Pimote sockets, and ThingSpeak.
# MIT license.
# http://bennet.org/blog/raspberry-pi-terrarium-controller/

# Imports
from gpiozero import Energenie

# Main lights off
lights = Energenie(2)
lights.off()