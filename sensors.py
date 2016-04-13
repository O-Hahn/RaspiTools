#!/usr/bin/python

#from grovepi import *
import grovepi


dht_sensor_port = 4		# Connect the DHt sensor to port D4
dht_sensor_type = 1

ultrasonic_port = 3 		# Connect Ultrasonic Ranger to port D3

sound_sensor_port = 0           # Connect Sound Sensor to port A0
grovepi.pinMode(sound_sensor_port,"INPUT")

[ temp,hum ] = grovepi.dht(dht_sensor_port,dht_sensor_type)		#Get the temperature and Humidity from the DHT sensor
t = str(temp)
h = str(hum)

d = str(grovepi.ultrasonicRead(ultrasonic_port))

s = str(grovepi.analogRead(sound_sensor_port))

print("{\"d\":{\"temp\":" + t + ",\"hum\":" + h + ",\"dist\":" + d  + ",\"snd\":" + s + "}}")			
