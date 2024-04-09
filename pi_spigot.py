# Stolen from: https://www.instructables.com/A-Spigot-That-Streams-Digits-of-Pi/

import re
import time
import argparse

import RPi.GPIO as GPIO

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

def pi_digits():
    "Generate n digits of Pi."
    k, a, b, a1, b1 = 2, 4, 1, 12, 4
    while True:
        p, q, k = k * k, 2 * k + 1, k + 1
        a, b, a1, b1 = a1, b1, p * a + q * a1, p * b + q * b1
        d, d1 = a / b, a1 / b1
        while d == d1:
            yield int(d)
            # n -= 1
            a, a1 = 10 * (a % b), 10 * (a1 % b1)
            d, d1 = a / b, a1 / b1

# for n, i in enumerate(pi_digits()):
#     if n % 80 == 0:
#         print()
#     print(i, end="", flush=True)
#     time.sleep(0.6)

nDigits = 8
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=nDigits, block_orientation=90,
                     rotate=0, blocks_arranged_in_reverse_order=True)

# start message
def startMessage():
    msg = "#PiDay"
    show_message(device, msg, fill="white", font=proportional(CP437_FONT))

startMessage()

piGen = pi_digits()
digitWindow = " " * nDigits
nPiDigits = 0

while True:
    virtual = viewport(device, width=device.width + 8, height=8)
    with canvas(virtual) as draw:
        for i in range(nDigits):
            text(draw, (i*8, 0), digitWindow[i], fill="white", font=CP437_FONT)

    if nPiDigits != 1 or nextDigit == ".":
        nextDigit = "{}".format(next(piGen))
        nPiDigits += 1
    else:
        nextDigit =  "."

    digitWindow = digitWindow[1:] + nextDigit 

    if nextDigit != ".":
        x = nDigits * 8
        for r in [3, 2, 1]:
        
            with canvas(virtual) as draw:
                text(draw, (8, 0), digitWindow, fill="white", font=CP437_FONT)
                for j in range(0, r):
                    draw.rectangle((x+j, j, x+7-j, 7-j), outline = "black")
            time.sleep(0.3)
