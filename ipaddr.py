#!/usr/bin/python

import netifaces as ni
from grove_lcd import *

ints = ni.interfaces()
for i in ints:
  if 'eth' in i:
    try:
      ni.ifaddresses(i)[2][0]['addr']
      setColor("blue")
      print("ETH Address:" + ni.ifaddresses(i)[2][0]['addr'])
      setText("IP Address:#" + ni.ifaddresses(i)[2][0]['addr'])
    except:
      pass
  elif 'wlan' in i:
    try:
      ni.ifaddresses(i)[2][0]['addr']
      setColor("blue")
      print("WLAN Address: " + ni.ifaddresses(i)[2][0]['addr'])
      setText("IP Address:#" + ni.ifaddresses(i)[2][0]['addr'])
    except:
      pass
