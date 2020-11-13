"""
    Number 4
"""

from microbit import *
from time import sleep

# dotPatterns =[[0,0],[1,0],[2,0],[3,0],[4,0],
#             [4,1],[4,2],[4,3],[4,4],[3,4],
#             [2,4],[1,4],[0,4],[0,3],[0,2],
#             [0,1],[1,1],[2,1],[3,1],[3,2],
#             [3,3],[2,3],[1,3],[1,2],[2,2]]
# while True: 
    #  for i in range (0,len(dotPatterns)):
#         display.set_pixel( dotPatterns[i][0], dotPatterns[i][1], 9)
#         print(dotPatterns)
#         sleep(0.5)
#         display.set_pixel(dotPatterns[i][0], dotPatterns[i][1], 0)

dotPatterns = [[0,0],[1,0],[2,0],[3,0],[4,0],
                [0,1],[1,1],[2,1],[3,1],[4,1],
                [0,2],[1,2],[2,2],[3,2],[4,2],
                [0,3],[1,3],[2,3],[3,3],[4,3],
                [0,4],[1,4],[2,4],[3,4],[4,4]]

while True:
    for i in range (0,len(dotPatterns)):
        display.set_pixel(dotPatterns[i][0], dotPatterns[i][1], 9)
        sleep(0.5)
        display.set_pixel(dotPatterns[i][0], dotPatterns[i][1], 0)