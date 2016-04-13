#!/usr/bin/python

from grovepi import *
from grove_lcd import *

dht_sensor_port = 4		# Connect the DHt sensor to port 7
dht_sensor_type = 1

while True:
	try:
		[ temp,hum ] = dht(dht_sensor_port,dht_sensor_type)		#Get the temperature and Humidity from the DHT sensor
		print "temp =", temp, "C\thumidity =", hum,"%" 	
		t = str(temp)
		h = str(hum)
                setColor("blue")
		setText("Temp:" + t + "C #" + "Humidity :" + h + "%")			
	except (IOError,TypeError) as e:
		print "Error"
