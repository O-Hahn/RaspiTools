#!/usr/bin/python
# grovepi + grove RGB LCD module
#http://www.seeedstudio.com/wiki/Grove_-_LCD_RGB_Backlight
#
# Just supports setting the backlight colour, and
# putting a single string of text onto the display
# Doesn't support anything clever, cursors or anything

'''
The MIT License (MIT)

GrovePi for the Raspberry Pi: an open source platform for connecting Grove Sensors to the Raspberry Pi.
Copyright (C) 2015  Dexter Industries

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''

import time,sys
import RPi.GPIO as GPIO
import smbus

DISPLAY_RGB_ADDR=0x62
DISPLAY_TEXT_ADDR=0x3e

# use the bus that matches your raspi version
rev = GPIO.RPI_REVISION
if rev == 2 or rev == 3:
    bus = smbus.SMBus(1)
else:
    bus = smbus.SMBus(0)

# set backlight to (R,G,B) (values from 0..255 for each)
def setRGB(r,g,b):
    bus.write_byte_data(DISPLAY_RGB_ADDR,0,0)
    bus.write_byte_data(DISPLAY_RGB_ADDR,1,0)
    bus.write_byte_data(DISPLAY_RGB_ADDR,0x08,0xaa)
    bus.write_byte_data(DISPLAY_RGB_ADDR,4,r)
    bus.write_byte_data(DISPLAY_RGB_ADDR,3,g)
    bus.write_byte_data(DISPLAY_RGB_ADDR,2,b)

# set background via text
def setColor(color):
    if color == "red":
        setRGB(255,0,0)
    elif color == "green":
        setRGB(0,255,0)
    elif color == "blue":
        setRGB(0,255,255)
    elif color == "yellow":
        setRGB(255,255,0)

# send command to display (no need for external use)    
def textCommand(cmd):
    bus.write_byte_data(DISPLAY_TEXT_ADDR,0x80,cmd)

# set display text \n for second line(or auto wrap)     
def setText(text):
  textCommand(0x01) # clear display
  time.sleep(0.05)
  textCommand(0x08|0x04) # display on, no cursor
  textCommand(0x28) # 2 lines
  time.sleep(0.05)
  count = 0
  row=0
  for c in text:
    if c=='#':
        count=0
        row=1
        textCommand(0xc0)
        continue
    if count==16 and row==0:
        textCommand(0xc0)
        row+=1
    count+=1
    bus.write_byte_data(DISPLAY_TEXT_ADDR,0x40,ord(c))


# example code
if __name__=="__main__":

  if len(sys.argv) > 1:
    setColor( sys.argv[1] )
    setText( " ".join(sys.argv[2:]) )
  else:
    print(" No arguments ")



