#!/usr/bin/env python3

# Control Adafruit Neo Trinkey (https://www.adafruit.com/product/4870)
# Neopixel LEDS over a serial interface.
# Based on script by Dave Parker https://github.com/daveparker/neotrinkey
# Adapted by Garrett Miller for CPU usage/process monitoring

import argparse
import sys
import serial
import psutil

DEFAULT_BAUD = 115200
DEFAULT_DEVICE = '/dev/serial/by-id/usb-Adafruit_Industries_LLC_NeoPixel_Trinkey_M0_7B5BCFA94150535020312E3815180BFF-if00'

COLOR_MAP = {
    'red':     'r',
    'yellow':  'y',
    'orange':  'o',
    'green':   'g',
    'teal':    't',
    'cyan':    'c',
    'blue':    'b',
    'purple':  'p',
    'magenta': 'm',
    'white':   'w',
    'black':   'blk',
    'off':     'blk',
    'gold':    'au',
    'pink':    'pk',
    'aqua':    'h2o',
    'jade':    'j',
    'amber':   'a',
    'oldlace': 'ol',
}

class NeoTrinkey:

    def __init__(self, baud, device):
        self.baud = baud
        self.device = device

    def send(self, command):
        with serial.Serial(self.device, baudrate=self.baud) as dev:
            dev.write('{}\r'.format(command).encode())

def main():
    #Loop forever
    while True:
        # Sample, update every x seconds
        cpu_utilization = psutil.cpu_percent(.5)
        neo_trinkey = NeoTrinkey(DEFAULT_BAUD, DEFAULT_DEVICE)
        #print('The CPU usage is: ', cpu_utilization)
        
        #TODO make this suck less
        redval = cpu_utilization/100 * 255 
        greenval = 255 - (cpu_utilization/100 * 255)

        #Send it, bro
        neo_trinkey.send(str(int(redval))+","+str(int(greenval))+","+"0")   

if __name__ == '__main__':
    main()
