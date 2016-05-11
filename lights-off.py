#!/usr/bin/python3

# lights-off.py - For Terrarium Controllers using Adafruit
# DHT sensors, Energenie Pimote sockets, and ThingSpeak.
# MIT license.
# http://bennet.org/blog/raspberry-pi-terrarium-controller/

# Imports
from gpiozero import Energenie

# Main lights off
lightsocket = 2
l = Energenie(lightsocket, initial_value=False)