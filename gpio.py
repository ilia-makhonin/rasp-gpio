#!/usr/bin/python
# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time

Relay_Pause1 = 0.1
Relay_Pause2 = 1

Relay_Ch1 = 26
Relay_Ch2 = 20
Relay_Ch3 = 21
Relay_Ch4 = 22
Relay_Ch5 = 23
Relay_Ch6 = 24

Relay_Ch7 = 19
Relay_Ch8 = 27

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(Relay_Ch1, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(Relay_Ch2, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(Relay_Ch3, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(Relay_Ch4, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(Relay_Ch5, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(Relay_Ch6, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(Relay_Ch7, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(Relay_Ch8, GPIO.OUT, initial=GPIO.HIGH)

print("Setup The Relay Module is [success]")

try:
    while True:
        #Control the Channel 1
        GPIO.output(Relay_Ch1,GPIO.LOW)
        print("Channel 1:The Common Contact is access to the Normal Open Contact!")
        time.sleep(Relay_Pause1)

        #Control the Channel 2
        GPIO.output(Relay_Ch2,GPIO.LOW)
        print("Channel 2:The Common Contact is access to the Normal Open Contact!")
        time.sleep(Relay_Pause1)

        #Control the Channel 3
        GPIO.output(Relay_Ch3,GPIO.LOW)
        print("Channel 3:The Common Contact is access to the Normal Open Contact!")
        time.sleep(Relay_Pause1)

        #Control the Channel 4
        GPIO.output(Relay_Ch4,GPIO.LOW)
        print("Channel 4:The Common Contact is access to the Normal Open Contact!")
        time.sleep(Relay_Pause1)

        #Control the Channel 5
        GPIO.output(Relay_Ch5,GPIO.LOW)
        print("Channel 5:The Common Contact is access to the Normal Open Contact!")
        time.sleep(Relay_Pause1)

        #Control the Channel 6
        GPIO.output(Relay_Ch6,GPIO.LOW)
        print("Channel 6:The Common Contact is access to the Normal Open Contact!")
        time.sleep(Relay_Pause1)

        #Control the Channel 7
        GPIO.output(Relay_Ch7,GPIO.LOW)
        print("Channel 7:The Common Contact is access to the Normal Open Contact!")
        time.sleep(Relay_Pause1)

        #Control the Channel 8
        GPIO.output(Relay_Ch8,GPIO.LOW)
        print("Channel 8:The Common Contact is access to the Normal Open Contact!")
        
        time.sleep(Relay_Pause2)

        GPIO.output(Relay_Ch1,GPIO.HIGH)
        print("Channel 1:The Common Contact is access to the Normal Closed Contact!\n")
        time.sleep(Relay_Pause1)

        GPIO.output(Relay_Ch2,GPIO.HIGH)
        print("Channel 2:The Common Contact is access to the Normal Closed Contact!\n")
        time.sleep(Relay_Pause1)

        GPIO.output(Relay_Ch3,GPIO.HIGH)
        print("Channel 3:The Common Contact is access to the Normal Closed Contact!\n")
        time.sleep(Relay_Pause1)

        GPIO.output(Relay_Ch4,GPIO.HIGH)
        print("Channel 4:The Common Contact is access to the Normal Closed Contact!\n")
        time.sleep(Relay_Pause1)

        GPIO.output(Relay_Ch5,GPIO.HIGH)
        print("Channel 5:The Common Contact is access to the Normal Closed Contact!\n")
        time.sleep(Relay_Pause1)

        GPIO.output(Relay_Ch6,GPIO.HIGH)
        print("Channel 6:The Common Contact is access to the Normal Closed Contact!\n")
        time.sleep(Relay_Pause1)

        GPIO.output(Relay_Ch7,GPIO.HIGH)
        print("Channel 7:The Common Contact is access to the Normal Closed Contact!\n")
        time.sleep(Relay_Pause1)

        GPIO.output(Relay_Ch8,GPIO.HIGH)
        print("Channel 8:The Common Contact is access to the Normal Closed Contact!\n")
        
        time.sleep(Relay_Pause2)
except:
	print("except")
	GPIO.cleanup()
