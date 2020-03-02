#!/usr/bin/python
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.output(21, 0)
while True:
  time.sleep(1)
  try:
    tFile = open('/sys/class/thermal/thermal_zone0/temp')
    temp = float(tFile.read())
    tempC = temp/1000
    print tempC
    if tempC > 46.5:
      GPIO.output(21, 1)
      print "HOT"
    else:
      GPIO.output(21, 0)
      print "COLD"

  except:
    tFile.close()
    GPIO.cleanup()
    exit
