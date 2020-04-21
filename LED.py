#!/usr/bin/python3
# File name   : LED.py
# Description : WS_2812
# Website     : based on the code from https://github.com/rpi-ws281x/rpi-ws281x-python/blob/master/examples/strandtest.py
# Author      : original code by Tony DiCola (tony@tonydicola.com)
# Date        : 2019/02/23
import time
from rpi_ws281x import *
import argparse
import time


# LED strip configuration:
LED_COUNT      = 3      # Number of LED pixels.
LED_PIN        = 12      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

#CUR_COLOR = 'white'

class LED:
    colors = [Color(255,255,255),
        Color(0,0,255),
        Color(0,255,0),
        Color(255,0,0),
        Color(0,0,0)]

    def __init__(self):
        self.LED_COUNT      = 16      # Number of LED pixels.
        self.LED_PIN        = 12      # GPIO pin connected to the pixels (18 uses PWM!).
        self.LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
        self.LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
        self.LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
        self.LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
        self.LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
        parser = argparse.ArgumentParser()
        parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
        args = parser.parse_args()

        # Create NeoPixel object with appropriate configuration.
        self.strip = Adafruit_NeoPixel(self.LED_COUNT, self.LED_PIN, self.LED_FREQ_HZ, self.LED_DMA, self.LED_INVERT, self.LED_BRIGHTNESS, self.LED_CHANNEL)
        # Intialize the library (must be called once before other functions).
        self.strip.begin()
        self.color_iter = iter(LED.colors)

    # Define functions which animate LEDs in various ways.
    def colorWipe(self, color):
        """Wipe color across display a pixel at a time."""
        #color = Color(R,G,B)
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, color)
            self.strip.show()

    def change_color(self):
        try:
            color = next(self.color_iter)
        except:
            color = LED.colors[0]
            self.color_iter = iter(LED.colors)
        self.colorWipe(color)

    def _police(self):
        timeout = time.time() + 5
        while True:
            self.colorWipe(Color(0,0,255))
            time.sleep(.1)
            self.colorWipe(Color(255,0,0))
            time.sleep(.1)
            if time.time()>timeout:
                break
    def _rainbow(self):
        timeout = time.time() + 5
        r,b,g = 0,0,0
        while True:
            for r in range(start,end,10):
                self.colorWipe(Color(r,g,b))
                time.sleep(.01)
            for b in range(start,end,10):
                self.colorWipe(Color(r,g,b))
                time.sleep(.01)
            for g in range(start,end,10):
                self.colorWipe(Color(r,g,b))
                time.sleep(.01)           

    def change_color_routine(self):
        self._police()