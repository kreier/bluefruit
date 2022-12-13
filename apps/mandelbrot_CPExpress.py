# mandelbrot on Circuit Playground Express TFT Gizmo
# It can't work since complex numbers are not supported.
# https://github.com/kreier/clue/app/mandelbrot.py
# 2022/11/16 v0.2

import board, displayio, random, math
from adafruit_gizmo import tft_gizmo

#display = board.DISPLAY
display = tft_gizmo.TFT_Gizmo()

# Create a bitmap with 256 colors
width = int(display.width / 2.6)
height = int(display.height / 2.6)

bitmap = displayio.Bitmap(width, height, 256)

def hsv_to_rgb(h, s, v):
    if s == 0.0: v*=255; return (v, v, v)
    i = int(h*6.)
    f = (h*6.)-i; p,q,t = int(255*(v*(1.-s))), int(255*(v*(1.-s*f))), int(255*(v*(1.-s*(1.-f)))); v*=255; i%=6
    if i == 0: ret = (65536*v + 256*t + p)
    if i == 1: ret = (65536*q + 256*v + p)
    if i == 2: ret = (65536*p + 256*v + t)
    if i == 3: ret = (65536*p + 256*q + v)
    if i == 4: ret = (65536*t + 256*p + v)
    if i == 5: ret = (65536*v + 256*p + q)
    #return f"{ret:06X}"
    return ret

# Create a 256 color palette
palette = displayio.Palette(256)
for i in range(256):
    #palette[i] = random.randrange(16777216)
    palette[i] = hsv_to_rgb(i/256, 1, 1)
palette[0] = 0

# Create a TileGrid using the Bitmap and Palette
tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette)

# Create a Group
group = displayio.Group()

# Add the TileGrid to the Group
group.append(tile_grid)

# Add the Group to the Display
display.show(group)

# Draw even more pixels
#for c in range(len(palette)):
#    for x in range(display.width):
#        for y in range(display.height):
#            bitmap[x, y] = (x + y) % 256

minX = -1.0
maxX = 0.5
aspectRatio = 1
ITERATION = 50
yScale = (maxX-minX)*(float(height)/width)*aspectRatio

for y in range(height):
    for x in range(width):
        c = math.sqrt((minX+x*(maxX-minX)/width) ** 2 + (y*yScale/height-yScale/2) ** 2)
#        c = complex(minX+x*(maxX-minX)/width, y*yScale/height-yScale/2)
        z = c
        for iter in range(ITERATION):
            if abs(z) > 2:
                break
            z = z*z+c
        if iter == ITERATION - 1:
            pixelcolor = 0
        else:
            pixelcolor = iter *5
        bitmap[x, y] = pixelcolor


# Loop forever so you can enjoy your image
while True:
    pass
