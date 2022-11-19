#!/usr/bin/env python3
import sys
import time

import json

from PIL import Image
import requests
from io import BytesIO

import ST7789 as ST7789

if len(sys.argv) < 2:
    print("""Usage: {} <display_type>

Where <display_type> is one of:
  * square - 240x240 1.3" Square LCD
  * round  - 240x240 1.3" Round LCD (applies an offset)
  * rect   - 240x135 1.14" Rectangular LCD (applies an offset)
  * dhmini - 320x240 2.0" Display HAT Mini 
""".format(sys.argv[0]))
    sys.exit(1)

try:
    display_type = sys.argv[1]
except IndexError:
    display_type = "square"

# Create ST7789 LCD display class.

if display_type in ("square", "rect", "round"):
    disp = ST7789.ST7789(
        height=135 if display_type == "rect" else 240,
        rotation=0 if display_type == "rect" else 90,
        port=0,
        cs=ST7789.BG_SPI_CS_FRONT,  # BG_SPI_CS_BACK or BG_SPI_CS_FRONT
        dc=9,
        backlight=19,               # 18 for back BG slot, 19 for front BG slot.
        spi_speed_hz=80 * 1000 * 1000,
        offset_left=0 if display_type == "square" else 40,
        offset_top=53 if display_type == "rect" else 0
    )

elif display_type == "dhmini":
    disp = ST7789.ST7789(
        height=240,
        width=320,
        rotation=180,
        port=0,
        cs=1,
        dc=9,
        backlight=13,
        spi_speed_hz=60 * 1000 * 1000,
        offset_left=0,
        offset_top=0
   )

else:
    print ("Invalid display type!")

WIDTH = disp.width
HEIGHT = disp.height

# Initialize display.
disp.begin()

def set_image():
    # Get the random Ingenuity photo
    image_file = None
    image_url = "https://picsum.photos/320/240"

    # Load an image.
    # print(f'Getting image: {image_url}...')

    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    
    # Draw the image on the display hardware.
    # print('Drawing image')

    disp.display(image)

while True:
    set_image()
    time.sleep(10)

