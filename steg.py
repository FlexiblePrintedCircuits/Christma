import sys
import os
from PIL import Image
import math

#opecode = "><+-.,[]#"
opecode = "CHRISTMA"

def to_binary(n) :
    return [math.floor(n / 9),math.floor(n / 3) % 3,n % 3]

#data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
data = []
for p in sys.argv[2] :
    data.append(opecode.find(p))


for x in data :
    print(to_binary(x))

img = Image.open("./" + sys.argv[1])
rgba_img = img.convert('RGBA')
size = rgba_img.size
result = Image.new('RGBA',size)
result.paste(rgba_img, (0, 0))

index = 0
flag = True

for y in range(size[1]) :
    for x in range(size[0]) :
        r,g,b,a = rgba_img.getpixel((x,y))
        
        r -= r % 3
        g -= g % 3
        b -= b % 3

        if(index < len(data)):
            bn = to_binary(data[index])

            r += bn[0]
            g += bn[1]
            b += bn[2]
        if(index == len(data)):
            r += 2
            g += 2
            b += 2

        index += 1
        
        result.putpixel((x,y),(r,g,b,a))

result.save(sys.argv[1] + "_steged.png")

def to_binary(n) :
    return [math.floor(n / 9),math.floor(n / 3) % 3,n % 3]

