import sys

# C -ポインタをインクリメント【 (p++) 】
# H -ポインタをデクリメント 【 (p--) 】
# R -ポインタの値をインクリメン ト【 (*p)++) 】
# I -ポインタの値をデクリメント【 (*p)++ 】
# S -ポインタの値を出力 【 putchar(*p); 】
# T -入力から1バイト読み込んでポインタが指す値に代入 【 *p = get() 】
# M -ポインタの指す値が0なら後のAまでジャンプ 【 if(*p == 0){ goto back } 】
# A -ポインタの指す値が0でなければ前のMまでジャンプ 【　if(*p == 0) { goto forward }　】