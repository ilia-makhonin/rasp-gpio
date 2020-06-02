import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

hallpin = 4
hallpin2 = 2

gpio.setup(hallpin, gpio.IN)
gpio.setup(hallpin2, gpio.IN, pull_up_down=gpio.PUD_DOWN)

while True:
      print(gpio.input(hallpin2))
      print(gpio.input(hallpin))
      print('------------------------------------------')
      time.sleep(0.3)
