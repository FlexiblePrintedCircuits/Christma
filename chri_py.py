# CHRISTMAのPythonインタプリンタ

# C -ポインタをインクリメント【 (p++) 】
# H -ポインタをデクリメント 【 (p--) 】
# R -ポインタの値をインクリメン ト【 (*p)++) 】
# I -ポインタの値をデクリメント【 (*p)++ 】
# S -ポインタの値を出力 【 putchar(*p); 】
# T -入力から1バイト読み込んでポインタが指す値に代入 【 *p = get() 】
# M -ポインタの指す値が0なら後のAまでジャンプ 【 if(*p == 0){ goto back } 】
# A -ポインタの指す値が0でなければ前のMまでジャンプ 【　if(*p == 0) { goto forward }　】

import sys

mem = [0 for i in range(10000)]
pointer = 0
program_counter = 0

# コマンドライン引数からファイルを取得
if __name__ == "__main__":
    args = sys.argv
    path = args[1]
    with open(path) as f:
        code = f.read()
    tape = list(code)

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
                if tape[program_counter] == '[':
                    nest += 1
                if tape[program_counter] == ']' and nest == 0:
                    break
                if tape[program_counter] == ']':
                    nest -= 1

    # A
    elif tape[program_counter] == 'A':
        if mem[pointer] != 0:
            nest = 0
            while True:
                program_counter -= 1
                if tape[program_counter] == ']':
                    nest += 1
                if tape[program_counter] == '[' and nest == 0:
                    break
                if tape[program_counter] == '[':
                    nest -= 1

    program_counter += 1