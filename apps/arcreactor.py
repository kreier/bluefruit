# Ironman Arc Reactor

import time
import board
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.4, auto_write=False)
minBrightness = 10
maxBrightness = 100
currentBrightness = minBrightness
step = (maxBrightness - minBrightness)/100

GOING_UP = 0
GOING_DOWN = 1
currentState = GOING_UP

def updateSystem():
    global currentState
    global currentBrightness

    if(currentState == GOING_UP):
        if(currentBrightness <= maxBrightness):
          currentBrightness += step
          # increase the brightness by step as long as the currentBrightness is less than the maximum.


    else:
        if(currentBrightness>minBrightness):
          currentBrightness -= step
          # decrease the brightness by step as long as the currentBrightness is greater than the minimum.



def evaluateState():
    global currentState
    global currentBrightness
    # If the current state is GOING_UP, and the current brightness is greater than the maximum brightness,
    if currentState == GOING_UP and currentBrightness > maxBrightness:
      currentState = GOING_DOWN
    # the state should change to GOING_DOWN.


    # If the current state is GOING_DOWN, and the current brightness is less than than the minimum brightness,
    if currentState == GOING_DOWN and currentBrightness < minBrightness:
      currentState = GOING_UP
    # the state should change to GOING_UP.


def reactToState():
    #light up the neopixels with the current brightness value.
    #Just do this for blue and green to get a good turqoise arc reactor color
    pixels.fill((0,round(currentBrightness),round(currentBrightness)))
    pixels.show()

while True:
    updateSystem()
    evaluateState()
    reactToState()
    time.sleep(0.01)
# Write your code here :-)
