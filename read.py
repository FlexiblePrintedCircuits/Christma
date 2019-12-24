import sys
import os
from PIL import Image
import math

#opecode = "><+-.,[]"
opecode = "CHRISTMA"

def from_binary(d) :
    return d[2] * 9 + d[1] * 3 + d[0]

#img = Image.open("couple_origin.png_steged.png")
img = Image.open(sys.argv[1])
rgba_img = img.convert('RGBA')
size = rgba_img.size

data = []
flag = True
index = 0

program = ""

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
            #print(opecode[value], end = "")
            program += opecode[value]

mem = [0 for i in range(10000)]
pointer = 0
program_counter = 0

# コマンドライン引数からファイルを取得
tape = program

while program_counter < len(tape):
    # C
    if tape[program_counter] == 'C':
        pointer += 1

    # H
    elif tape[program_counter] == 'H':
        pointer -= 1

    # R
    elif tape[program_counter] == 'R':
        mem[pointer] += 1

    # I
    elif tape[program_counter] == 'I':
        mem[pointer] -= 1

    # S
    elif tape[program_counter] == 'S':
        print(chr(mem[pointer]), end="")

    # T
    elif tape[program_counter] == 'T':
        mem[pointer] = int(input())

    # M
    elif tape[program_counter] == 'M':
        if mem[pointer] == 0:
            nest = 0
            while True:
                program_counter += 1
                if tape[program_counter] == 'M':
                    nest += 1
                if tape[program_counter] == 'A' and nest == 0:
                    break
                if tape[program_counter] == 'A':
                    nest -= 1

    # A
    elif tape[program_counter] == 'A':
        if mem[pointer] != 0:
            nest = 0
            while True:
                program_counter -= 1
                if tape[program_counter] == 'A':
                    nest += 1
                if tape[program_counter] == 'M' and nest == 0:
                    break
                if tape[program_counter] == 'M':
                    nest -= 1

    program_counter += 1

        
