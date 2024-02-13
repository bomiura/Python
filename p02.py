# -*- coding: utf-8 -*-
#
a,b= map(int, input().split())
c = a * b 
if c %  2 ==  0:
    d = "Even"
elif c % 2 == 1:
    d = "Odd"
print(d)
