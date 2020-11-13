from adafruit_circuitplayground import cp
from time import sleep

cp.pixels.brightness = 1
start = 0

while True:
    # if (start == 0 and start == 9):
    #     cp.pixels[start] =(255,255,255)
    #     sleep(1)
    # else:

        if (start == 0 or start == 9 ):
            cp.pixels[0] = (255,255,255)
            cp.pixels[9] = (255,255,255)
            sleep(1)
            cp.pixels[0]=0
            start = 9
        if ( start == 4):
            cp.pixels[5] = (255,255,255)
            cp.pixels[4] = (255,255,255)
            sleep(1)
            cp.pixels[5] = 0
            start = 4
        cp.pixels[start] = (255,255,255)
        sleep(1)
        cp.pixels[start] = 0
        start -=1

