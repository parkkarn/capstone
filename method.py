import RPi.GPIO as GPIO
import time
import requests
import json

def getCo2(PWM_PIN):
    GPIO.wait_for_edge(PWM_PIN, GPIO.FALLING)
    start = time.time()

    GPIO.wait_for_edge(PWM_PIN, GPIO.RISING)
    end = time.time()
    duration = end - start
    
    ppm = (1-duration) / 0.0002
    return int(ppm)

def giveWater(pin1, pin2):
    GPIO.output(pin1, GPIO.HGIH)
    GPIO.output(pin2, GPIO.HIGH)

def stopWater(pin1, pin2):
    GPIO.output(pin1, GPIO.LOW)
    GPIO.output(pin2, GPIO.LOW)

