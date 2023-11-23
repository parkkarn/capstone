import RPi.GPIO as GPIO
import time
import board
from method import *

#BCM
water1 = 17
water2 = 27

#GPIO.setup(button,GPIO.IN) # KY-004
GPIO.setup(water1, GPIO.OUT) 
GPIO.setup(water2, GPIO.OUT)

try:
    giveWater(water1,water2)
    time.sleep(150)
    stopWater(water1,water2)
except KeyboardInterrupt:

GPIO.cleanup()
