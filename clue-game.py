"""
Number 7
"""

from adafruit_clue import clue
from adafruit_clue import board
from time import sleep, time
from random import seed
from random import randint


clue_display = clue.simple_text_display(text_scale=2,)


# for i in range(3,-1,-1):
    
#     clue_display.show()
clue_display[0].text = "REACTION GAME"
clue_display[0].color = clue.ORANGE
clue_display[2].text = "Instructions:"
clue_display[2].color = clue.GREEN
clue_display[3].text = "Player A presses A"
clue_display[3].color = clue.WHITE
clue_display[4].text = "Player B presses B"
clue_display[4].color = clue.WHITE
clue_display[5].text = "Press if the numer"
clue_display[5].color = clue.SKY
clue_display[6].text = " is divisible by 2"
clue_display[6].color = clue.SKY
clue_display[7].text = "Maximum score of 5"
clue_display[7].color = clue.YELLOW


counter = 3
playerScoreA = 0
playerScoreB = 0

while True:
    clue_display.show()
    if(counter > -1):
        clue_display[8].text = "Starts in " + str(counter)
        clue_display[8].color = clue.ORANGE
        counter-= 1

    else:
        clue_display[2].text = ""
        clue_display[3].text = ""
        clue_display[4].text = ""
        clue_display[5].text = ""
        clue_display[6].text = ""
        clue_display[7].text = f"Score A: {playerScoreA}"
        clue_display[8].text = f"Score B: {playerScoreB}"
        
        

        if playerScoreA == 5 or playerScoreB == 5:
            clue_display[2].text = f"{'Player A' if playerScoreB < playerScoreA else 'Player B'}"
            clue_display[3].text = "     Win the Game!"
        else:
            ranNum = randint(0,100)
            clue_display[3].text = f"         {ranNum}"

        measure1 = time()
        measure2 = time()    
        while True:
            if(measure1 - measure2 >= 0.6):
                break;
            measure1 = time()

            if clue.button_a:
                print("clicked a")
                if ranNum % 2 == 0:
                    playerScoreA = playerScoreA + 1
                else :
                    playerScoreA = 0 if playerScoreA - 1 <= 0 else playerScoreA - 1
                break
                
            if clue.button_b:
                print("clicked b")
                if ranNum % 2 == 0:
                    playerScoreB = playerScoreB + 1
                else :
                    playerScoreB = 0 if playerScoreB - 1 <= 0 else playerScoreB - 1 
                break
            clue_display[7].text = f"Score A: {playerScoreA}"
            clue_display[8].text = f"Score B: {playerScoreB}"

    # clue_display.show()

        # if clue.button_a:
        #     print("press")
        # #    if ranNum % 2 == 0:
        # #        playerScoreA = playerScoreA + 1
        # else:
        #         # playerScoreA = playerScoreA - 1
        #         print("not")



    # if btnA == True  and ranNum % 2 == 0 :
    #     playerScoreA = playerScoreA + 1
    # else:
    #     playerScoreA = playerScoreA -1

    # if btnB and ranNum % 2 == 0 :
    #     playerScoreB = playerScoreB + 1
    # else:
    #     playerScoreB = playerScoreB -1


    

    # clue_display[5].text = "Player A Score: " + str(playerScoreA)
    # clue_display[5].color = clue.GREEN

    # clue_display[6].text = "Player B Score: " + str(playerScoreB)
    # clue_display[6].color = clue.SKY


    