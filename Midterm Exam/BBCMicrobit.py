from microbit import *
from time import sleep

first = Image("90000:09000:00900:00090:00009")
second = Image("09000:00900:00090:00009:90000")
third = Image("00900:00090:00009:90000:09000")
fourth = Image("00090:00009:90000:09000:00900")
fifth = Image("00009:90000:09000:00900:00090")

final = [first,second,third,fourth,fifth]

while True:
    for i in range(0,len(final)):
        display.show(final)
        sleep(0.2)
    
