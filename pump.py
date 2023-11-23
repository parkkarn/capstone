import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)

try:
    GPIO.output(12, 1)
    time.sleep(150)
    GPIO.output(12, 0)

finally:
    GPIO.cleanup()
