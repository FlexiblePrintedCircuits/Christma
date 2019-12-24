import sys
import os
from PIL import Image
import math

opecode = "><+-.,[]"

def from_binary(d) :
    return d[2] * 9 + d[1] * 3 + d[0]

#img = Image.open("couple_origin.png_steged.png")
img = Image.open(sys.argv[1])
rgba_img = img.convert('RGBA')
size = rgba_img.size

data = []
flag = True
index = 0

for y in range(size[1]) :
    for x in range(size[0]) :
        r,g,b,a = rgba_img.getpixel((x,y))

        x = [0] * 3
        x[2] = r % 3
        x[1] = g % 3
        x[0] = b % 3

        value = from_binary(x)
    
        if(value == 26) :
            flag = False
        
        if(flag) :
            print(opecode[value])


        
