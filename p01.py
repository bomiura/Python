# -*- coding: utf-8 -*-

a = int(input())
b, c= map(int, input().split())
d = input()

e = a + b + c 
# print(str(e) + " " + d)
print("{} {}".format(a+b+c,d))
""

# ヒアドキュメント
lines = '''
    このように
    複数行
    記述できます

    改行が入れたくない場合、 \
    末尾にバッククオート(\)をつけて

# -*- coding: utf-8 -*-
# 整数の入力
a = int(input())
# スペース区切りの整数の入力
b, c = map(int, input().split())
# 文字列の入力
s = input()
# 出力
print("{} {}".format(a+b+c, s))

'''
