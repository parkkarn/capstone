import RPi.GPIO as GPIO
import board
import adafruit_dht as dht
import json
from method import *


#BCM
PWM_PIN = 18
mydht = dht.DHT11(board.D23) #DHT11

GPIO.setmode(GPIO.BCM)

GPIO.setup(PWM_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)


try:
    h = mydht.humidity
    t = mydht.temperature
    ppm = getCo2(PWM_PIN)
        
    sensor_data = {
            'temp' : t,
            'humi' : h,
            'CO2' : ppm
    }
    GPIO.cleanup()

    with open('data.json', 'w') as json_file:
        json.dump(sensor_data, json_file)
except RuntimeError:
    GPIO.cleanup()


