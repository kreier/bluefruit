# Ten circulating NeoPixel example
import time, board, neopixel
from digitalio import DigitalInOut, Direction, Pull

button = DigitalInOut(board.BUTTON_B)
button.direction = Direction.INPUT
button.pull = Pull.DOWN

num_pixels = 10

neo = neopixel.NeoPixel(board.NEOPIXEL, num_pixels, brightness=0.1, auto_write=False)

while not button.value:
    for x in range(10):
        for y in range(10):
            if x == y:
                neo[y] = (255,0,0)
            else:
                neo[y] = (0,0,0)
        time.sleep(0.02)
        neo.show()

print("Aborted")
