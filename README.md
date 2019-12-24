# - Christma -
トラック倒し、バイトテロ、童貞いじり...<br>
何かあったらすぐに炎上してしまう、世知辛いデジタルの時代、私たちクリぼっちがクリスマスに一人でいるなんてことが全国のリア充どもに知られたら、総攻撃を受けるに違いありません(偏見)<br>
いつもの音ゲーのリザルトも、萌え絵も、くだらないコラもツイートすることすらできなくなってしまうのです！<br>
しかし、そんな全国のボッチ達の悲壮な声にならない叫びを聞き、それらの問題を解決するプロダクトを作りました。<br>
**画像にプログラムを隠し**、さらにインタプリタがないと**実行すらできない**という徹底された隠蔽...現代の辛い若者達のために作られた対リア充最終防衛ライン。その名も<br>
**C R I S T M A** です。<br>
書いたあとに何やってんだ僕ってなった。(by.Iwancof)

# 概要
CとRとIとSとTとMとAのわずか8種類の命令でプログラムを書くことのできる、Brainfuckにインスパイアを受けたプログラミング言語です。<br>
全てのクリぼっちに捧げる言語として設計されました。<br>

# 言語仕様

| 文字 | 操作 |
|------|------|
| C | ポインタをインクリメント |
| H | ポインタをデクリメント |
| R | ポインタの値をインクリメント |
| I | ポインタの値をデクリメント |
| S | 現在のポインタの値を出力 |
| T | 入力から1バイト読み込みポインタが指す値に代入 |
| M | ポインタの値が0なら、次のAまで飛ぶ |
| A | ポインタの値が0じゃなかったら、前のMまで飛ぶ |

# 実行
C++とPython製のインタプリンタをとりあえず用意しています。<br>
実行対象の.chriファイルを第一引数として渡すだけです。

[C++］
```
a.exe hoge.chri
```
[Python］
```
python read.py hoge.chri
```
※ read.pyでの実行にはpillowというモジュールが必要です。<br>
pipでインストールできますができない場合はchri_py.pyでも実行できます。
# 機能
各インタプリンタには実行の他にも以下の機能が備わっています。<br>

| インタプリンタ | 機能 |
|------|------|
| C++ | 引数を指定せずに実行するとクリスマスツリーのAAが表示される |
| Python | Christmaのコードが隠し埋め込まれた画像を復号・生成する<br> [復号] python read.py hoge.png<br>[生成] python steg.py poyo.png hoge.chri|

# メンバー

[FPC_COMMUNITY]: https://twitter.com/FPC_COMMUNITY
[iwancof_ptr]: https://twitter.com/Iwancof_ptr
[e381x]: https://twitter.com/e381x
[FlexiblePrintedCircuits][FPC_COMMUNITY]/
[iwancof][iwancof_ptr]/
[kakao][e381x]
