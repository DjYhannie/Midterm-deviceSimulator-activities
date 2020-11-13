"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.
Get started with micro:bit and MicroPython on:
https://microbit-micropython.readthedocs.io/en/latest/.
"""

from microbit import *
from time import sleep

while True:
    # display.show(Image("90000:00000:00000:00000:00000"))
    # sleep(1)
    # display.show(Image("60000:00000:00000:00000:00000"))
    # sleep(1)
    # display.show(Image("30000:00000:00000:00000:00000"))
    # sleep(1)
    # display.show(Image("00000:00000:00000:00000:00000"))
    # sleep(1)

    # display.set_pixel(0, 0, 9)
    # sleep(1)
    # display.set_pixel(0, 0, 6)
    # sleep(1)
    # display.set_pixel(0, 0, 3)
    # sleep(1)
    # display.set_pixel(0, 0, 0)
    # sleep(1)

    # light = display.read_light_level()
    # print("{}".format(light))
    # sleep(0.2)

    # light = display.read_light_level()
    # if light < 10:
    #     display.set_pixel(0, 0, light)
    # else:
    #     display.set_pixel(0, 0, 9)

    light = display.read_light_level()
    if light < 10:
        display.show(Image("{}0000:00000:00000:00000:00000".format(light)))
    else:
        display.show(Image("90000:00000:00000:00000:00000"))