# Displays a random Curiosity photo on a ST7789 screen

Ok, so first things first, 'what is a "Halina?"'.
A Halina is a old-timey Colour Slide viewer for 35mm photo slides.
It looks remarkably like a fancy looking 60/70's TV monitor so (without damaging anything) I've modded it to hold a Raspberry Pi zero along with a tiny 320 x 240 LCD screen.

I have some quiet plans for it, but to at least get it to do something with a 'wow' factor I've thrown together a simple script to get a random Ingenuity photo every 10 seconds.
Oh and now there is a random_photo.py version that gets a random photo from picsum.photos. :)

It uses the ST7789 library from Adafruit, code adapted from [Pimoroni's ST7789 library](https://github.com/pimoroni/st7789-python).

I'm using a dhmini so to run it I use: `python ingenuity_random-image.py dhmini`
