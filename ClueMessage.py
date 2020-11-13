
"""
Number 6
"""
from adafruit_clue import clue
from time import sleep

# myTitle = clue.simple_text_display(title= "Message Streamer", title_scale= 3 , title_color= (clue.RED,))


clue_display = clue.simple_text_display(text_scale=2,)
msg1 = " This message move from right to left "
msg2 =  " This message moves from left to right "

while True:
    clue_display[0].text = "Message Streamer"
    clue_display[0].color = clue.RED

    clue_display[2].text = msg1
    clue_display[2].color = clue.YELLOW

    temp = msg1[0]
    msg1 = msg1[1:] + temp

    clue_display[4].text = msg2
    clue_display[4].color = clue.WHITE

    temp = msg2[len(msg2)-1]
    msg2 = temp + msg2[:-1] 

    clue_display[6].text = "This message blinks"
    clue_display[6].color = clue.SKY
    clue_display.show()
    sleep(0.5)
    clue_display[6].color = clue.BLACK  
    