# -*- coding: utf-8 -*-

a,b,c= map(int, input().split())
t = a * b
if t < c:
    print(t)
else:
    print(c)
