import sys
import os
from PIL import Image
import math


def to_binary(n) :
    return [math.floor(n / 4),math.floor(n / 2) % 2,n % 2]

data = [1,1,4,5,1,4,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,3,6,4,3,6,4]

for x in data :
    print(to_binary(x))

img = Image.open("./image.png")
rgba_img = img.convert('RGBA')
size = rgba_img.size
result = Image.new('RGBA',size)
result.paste(rgba_img, (0, 0))

index = 0
flag = True

for y in range(size[1]) :
    for x in range(size[0]) :
        r,g,b,a = rgba_img.getpixel((x,y))
        
        if(index < len(data)):
            bn = to_binary(data[index])
            index += 1

            if(bn[0] == 0) :
                r += r % 2
            else :
                r += 1 - r % 2

            if(bn[1] == 0) :
                g += g % 2
            else :
                g += 1 - g % 2

            if(bn[2] == 0) :
                b += b % 2
            else :
                b += 1 - b % 2

        result.putpixel((x,y),(r,g,b,a))

result.save("tmp.png")



def to_binary(n) :
    return [math.floor(n / 4),math.floor(n / 2) % 2,n % 2]

