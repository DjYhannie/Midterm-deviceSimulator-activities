# number 1



"""This project focuses on neopixels ."""
from adafruit_circuitplayground import cp
from time import sleep
 
cp.pixels.brightness = 1 
i = 0
while True:
    # # ...............................................
    #  other way of solving.....
    # if (i<0):
    #     i=9
    # else:
    #     i=i
    # if (i>9):
    #     i = 0
    # if cp.switch == False:
    #     cp.pixels[i] = (255,255,255 )
    #     sleep(0.5)
    #     cp.pixels[i] = (0,0,0)
    #     i-=1
    # else:
    #    cp.pixels[i] = (255,255,255)
    #    sleep(0.5)
    #    cp.pixels[i] = (0,0,0)
    #    i+=1
    
    # # print(i)
# ...........................................................

# from adafruit_circuitplayground import cp
# import time

# while True:
#     color = int(255 * cp.light / 320)
#     cp.pixels[0] = (color, color, color)
#     cp.pixels[1] = (color, color, color)
#     cp.pixels[2] = (color, color, color)
#     cp.pixels[3] = (color, color, color)
#     cp.pixels[4] = (color, color, color)
#     cp.pixels[5] = (color, color, color)
#     cp.pixels[6] = (color, color, color)
#     cp.pixels[7] = (color, color, color)
#     cp.pixels[8] = (color, color, color)
#     cp.pixels[9] = (color, color, color)

#     print(color)
#     time.sleep(0.5)


    if (i == -1):
        i = 9
    if (i >= 10):
        i = 0

    cp.pixels[i] = (255,255,255)
    sleep(0.5)
    cp.pixels[i] = 0


    if cp.switch:
        i -= 1
    else: i += 1
    