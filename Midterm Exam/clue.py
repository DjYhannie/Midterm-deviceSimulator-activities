from adafruit_clue import clue
from time import sleep


clue_display = clue.simple_text_display(text_scale=2,)
message = "This is a message. "

while True:
    clue_display[2].text = message
    clue_display[2].color = clue.AQUA

    temp = message[0]
    message = message[1:] + temp
    clue_display.show()
    sleep(1)
    clue_display[2].color = clue.BLACK