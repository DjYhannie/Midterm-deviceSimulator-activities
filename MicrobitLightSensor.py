"""

Number 5
"""



from microbit import *
from time import sleep

while True:
    light = display.read_light_level()  # display dot
    controlBrightness = (light//10)*10  # 
    brightness = light-controlBrightness

    positionController = light // 50
    
    y = 4 - positionController
    x = (light - (positionController * 50))// 10


    for i in range(5): # loops through the y axis
        if y < i:      # check if y is less than x
            for j in range(5): # loops through the x axis
                display.set_pixel(j,i,9)
        if y > i: # check if the y greater than i
            for j in range(5):# loops through the x axis
                display.set_pixel(j,i,0)
        if y == i: # check if the y is equal to i
            for j in range(5):# loops through the x axis
                if x < j:
                    display.set_pixel(j,i,0)
                if x > j:
                    display.set_pixel(j,i,9)
    if y == -1:
        display.set_pixel(4,0,9)
    else:
        display.set_pixel(x,y, brightness)

