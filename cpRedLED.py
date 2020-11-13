
# import CPX library
from adafruit_circuitplayground import cp
from time import sleep

while True:
    cp.red_led = True
    sleep(1)
    cp.red_led = False
    sleep(1)