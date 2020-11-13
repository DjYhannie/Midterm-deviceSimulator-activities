"""
    Number 3
"""

from microbit import display, Image
from time import sleep

ndx = 0
while True:
    if ndx > 28:
        ndx = 0
    lead = "00000:00000:00000:00000:00000"
    leadlist = list(lead)
    for i in range (0, len(leadlist)):
        if leadlist[i] == ':':
            continue
        if i == ndx:
            leadlist[i] = '9'
        else:
            leadlist[i] = '0'
    ndx = ndx +1
    lead = "".join(leadlist)
    display.show(Image(lead))
    sleep(0.5)