# Control Neo Trinkey (https://www.adafruit.com/product/4870)
# Neopixel LEDS over a serial interface.
# Set color and brightness (intensity) of each LED.
# Based on script by Dave Parker https://github.com/daveparker/neotrinkey
# Adapted by Garrett Miller for CPU usage/process monitoring

import neopixel
import board
import color
import supervisor
import time

NUM_PIXELS = 4
DEFAULT_INTENSITY = 0.5

COLOR_MAP = {
    "r": color.RED,
    "y": color.YELLOW,
    "o": color.ORANGE,
    "g": color.GREEN,
    "t": color.TEAL,
    "c": color.CYAN,
    "b": color.BLUE,
    "p": color.PURPLE,
    "m": color.MAGENTA,
    "w": color.WHITE,
    "blk": color.BLACK,
    "au": color.GOLD,
    "pk": color.PINK,
    "h2o": color.AQUA,
    "j": color.JADE,
    "a": color.AMBER,
    "ol": color.OLD_LACE,
}


pixels = neopixel.NeoPixel(
    board.NEOPIXEL,
    NUM_PIXELS,
    brightness=0.2,
    auto_write=False,
    pixel_order=neopixel.GRB,
)

pixels.fill(color.BLACK)
pixels.show()

colors = [color.BLACK] * NUM_PIXELS
intensities = [DEFAULT_INTENSITY] * NUM_PIXELS

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b)

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(NUM_PIXELS):
            pixel_index = (i * 256 // NUM_PIXELS) + j
            pixels[i] = wheel(pixel_index & 255)
        print(pixels)
        pixels.show()
        time.sleep(wait)

def serial_read():
    if supervisor.runtime.serial_bytes_available:
        return input()
    return None

def main():
    while True:
        data = serial_read()
        if data is None:
            #rainbow_cycle(0.001)
            continue
        #Cast our list sent over serial into ints and display it on all LEDs
        for i in range(NUM_PIXELS):
            listNumbers = [int(x) for x in list(data.split(','))]
            pixels[i] = listNumbers
        pixels.show()

if __name__ == "__main__":
    main()
