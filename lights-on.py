#!/usr/bin/python

# lights-on.py - For Terrarium Controllers using Adafruit
# DHT sensors, Energenie Pimote sockets, and ThingSpeak.
# MIT license.
# http://bennet.org/blog/raspberry-pi-terrarium-controller/

# Imports
import energenie

# Main lights off
lightsocket = 2
energenie.switch_on(lightsocket)