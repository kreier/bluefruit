# initialize the display
#import displayio
#from adafruit_gizmo import tft_gizmo
#display = tft_gizmo.TFT_Gizmo()

print("Knightrider example")

# CircuitPython Essentials NeoPixel example
import time, board, neopixel
from rainbowio import colorwheel

pixel_pin = board.NEOPIXEL
num_pixels = 10

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.1, auto_write=False)



def color_chase(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.5)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = colorwheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)


RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)

for i in range(7):
    for x in range(10):
        for y in range(10):
            if x == y:
                pixels[y] = (255,0,0)
            else:
                pixels[y] = (0,0,0)
        time.sleep(0.02)
        pixels.show()

for i in range(7):
    for x in range(10):
        for y in range(10):
            if x > y:
                pixels[y] = (255,0,0)
            else:
                pixels[y] = (0,0,0)
        time.sleep(0.02)
        pixels.show()
    for x in range(10):
        for y in range(10):
            if x < y:
                pixels[y] = (255,0,0)
            else:
                pixels[y] = (0,0,0)
        time.sleep(0.02)
        pixels.show()

def colorring(color):
    for x in range(10):
        for y in range(10):
            if x < 6:
                if y >= x and y < x + 5:
                    pixels[y] = color
                else:
                    pixels[y] = (0,0,0)
            else:
                if y >= x or y < x - 5:
                    pixels[y] = color
                else:
                    pixels[y] = (0,0,0)
        time.sleep(0.05)
        pixels.show()

for i in range(5):
    colorring(RED)
    colorring(YELLOW)
    colorring(GREEN)
    colorring(CYAN)
    colorring(BLUE)
    colorring(PURPLE)


for i in range(2):
#while True:
    pixels.fill(RED)
    pixels.show()
    # Increase or decrease to change the speed of the solid color change.
    time.sleep(0.1)
    pixels.fill(GREEN)
    pixels.show()
    time.sleep(0.1)
    pixels.fill(BLUE)
    pixels.show()
    time.sleep(0.1)

    color_chase(RED, 0.01)  # Increase the number to slow down the color chase
    color_chase(YELLOW, 0.01)
    color_chase(GREEN, 0.01)
    color_chase(CYAN, 0.01)
    color_chase(BLUE, 0.01)
    color_chase(PURPLE, 0.01)

    rainbow_cycle(0)  # Increase the number to slow down the rainbow
