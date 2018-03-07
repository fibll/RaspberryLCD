#!/usr/bin/python

import time
from Adafruit_CharLCD import *

PIN_RS  = 25
PIN_EN  = 24
PIN_DB4 = 23
PIN_DB5 = 17
PIN_DB6 = 27
PIN_DB7 = 22


if __name__ == '__main__':
  print "LCD Test Program"

  display = Adafruit_CharLCD(PIN_RS, PIN_EN, PIN_DB4, PIN_DB5, PIN_DB6, PIN_DB7, 16, 2)
  #display.enable_display(True)
  #display.home()
  display.clear() 
  #display.message("Hallo!")

  while 1:
    print ">",
    cmd = raw_input()

    if cmd == "home" or cmd == "h" :
      display.home()
    elif cmd == "clear" or cmd == "c":
      display.clear()
    elif cmd == "enable" or cmd == "e":
      display.enable_display(True)
    elif cmd == "disable" or cmd == "d":
      display.enable_display(False)
    elif cmd == "show" or cmd == "s":
      display.show_cursor(True)
    elif cmd == "blink" or cmd == "b":
      display.blink(True)
    elif cmd == "left" or cmd == "l":
      display.move_left()
    elif cmd == "right" or cmd == "r":
      display.move_right()
    elif cmd == "autoscroll" or cmd == "a":
      display.autoscroll(True)
    elif cmd == "p":
      display.message("Hallo Paula :)")
    elif cmd == "message" or cmd == "m":
      display.message("Legalize Weed!1234569123445\n123456789\nYou are nice")
    elif cmd == "1":
      i = 0
      while 1:
        display.home()
        display.clear()
        if i % 2 == 0:
          display.message(time.strftime("    %H:%M:%S"))
        else:
          display.message(time.strftime("\n    %H:%M:%S"))
        i +=1

        time.sleep(1)

        #print time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t))
    elif cmd == "2":
      display.home()
      display.clear()
      i = 0
      while 1:
        display.home()
        display.message(str(i))
        i += 1
    elif cmd == "quit" or cmd == "q":
      break
    else:
      print "Command '",cmd,"' not found"
