#!/usr/bin/python

import netifaces as ni
import socket as so

from grove_lcd import *

hostname = so.gethostname() 
ints = ni.interfaces()
for i in ints:
  if 'eth' in i:
    try:
      ni.ifaddresses(i)[2][0]['addr']
      setColor("blue")
      print(hostname + " ETH Address:" + ni.ifaddresses(i)[2][0]['addr'])
      setText(hostname + "#" + ni.ifaddresses(i)[2][0]['addr'])
    except:
      pass
  elif 'wlan' in i:
    try:
      ni.ifaddresses(i)[2][0]['addr']
      setColor("blue")
      print(hostname + " WLAN Address: " + ni.ifaddresses(i)[2][0]['addr'])
      setText(hostname + "#" + ni.ifaddresses(i)[2][0]['addr'])
    except:
      pass
