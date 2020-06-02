#!/usr/bin/python
# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time
import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

Relay_Ch1 = 26
Relay_Ch2 = 20
Relay_Ch3 = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(Relay_Ch1,GPIO.OUT)

print("Setup The Relay Module is [success]")

try:
    while True:
    #    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    #    if temperature is not None and int(temperature) < 30:
    #        GPIO.output(Relay_Ch1,GPIO.LOW)
    #        print("Channel 1:The Common Contact is access to the Normal Open Contact!")
    #        print(int(temperature))
    #    else:
    #        GPIO.output(Relay_Ch1,GPIO.HIGH)
    #        print("Channel 1:The Common Contact is access to the Normal Closed Contact!\n")
    #        print(int(temperature))
    #        time.sleep(8)
        GPIO.output(Relay_Ch1,GPIO.LOW)
except:
    print("except")
    GPIO.output(Relay_Ch1,GPIO.HIGH)
    GPIO.cleanup()

