import os
import time
from smbus import SMBus

DEV_ADDR = 0x48
adc_channels = {
    'AIN0':0b1000000, # 0x40 (foto-resistor)
    'AIN1':0b1000001, # 0x41 (thermistor)
    'AIN2':0b1000010, # 0x42 (not connected)
    'AIN3':0b1000011, # 0x43 (variable resistor)
}
dac_channel = 0b1000000 # 0x40

bus = SMBus(1)          # 1 for RPi model B rev.2
tmp = 0

while(1):
    os.system('clear')
    print("Press Ctrl C to stop...\n")
    for channel in adc_channels:
        # read value from ADC input
        bus.write_byte(DEV_ADDR, adc_channels[channel])
        value = bus.read_byte(DEV_ADDR)
        print ('Channel ' + channel + ' ---> ' + str(value))
    time.sleep(0.1)