import os
import time
import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

try:
    f = open('./humidity.csv', 'a+')
    if os.stat('./humidity.csv').st_size == 0:
        f.wrtite('Date,Time,Temperature,Humidity\r\n')
except:
    pass

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        f.write('{},{},{}*C,{}%\r\n'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'), temperature, humidity))
    else:
        print("Failed to retrieve data from humidity sensor")
        time.sleep(30)
