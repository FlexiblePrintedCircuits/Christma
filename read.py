import sys
import os
from PIL import Image
import math

def from_binary(d) :
    return d[2] * 4 + d[1] * 2 + d[0]

img = Image.open("tmp.png")
rgba_img = img.convert('RGBA')
size = rgba_img.size

data = []
flag = True
index = 0

for y in range(size[1]) :
    for x in range(size[0]) :
        r,g,b,a = rgba_img.getpixel((x,y))

        if(index > 50) :
            flag = False

        index += 1
        
        if(flag) :
            x = [0] * 3
            x[2] = r % 2
            x[1] = g % 2
            x[0] = b % 2
            print(from_binary(x))


        
