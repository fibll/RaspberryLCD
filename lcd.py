#!/usr/bin/python

#from Adafruit_CharLCD import *
import Adafruit_CharLCD as LCD

#PIN_RS  = 27
#PIN_EN  = 22
#PIN_DB4 = 25
#PIN_DB5 = 24
#PIN_DB6 = 23
#PIN_DB7 = 18

PIN_RS  = 25
PIN_EN  = 24
PIN_DB4 = 23
PIN_DB5 = 17
PIN_DB6 = 27
PIN_DB7 = 22


if __name__ == '__main__':
  print "LCD Test Program"

  display = LCD.Adafruit_CharLCD(PIN_RS, PIN_EN, PIN_DB4, PIN_DB5, PIN_DB6, PIN_DB7, 16, 2)
  #display.enable_display(True)
  #display.home()
  #display.clear() 
  display.message('Hallo!\nRaphael')

  print "[i] Initialized Display"
