# -*- coding: utf-8 -*-
a,b= map(int, input().split())
c = str(a) + str(b)
# print(c)
result = int(c) ** 0.5 # 平方根
# print(result)
if  isinstance(result, float):
    print("Yes")
else:
    print("No")

# lines = '''
# a, b = input().split()
# n = int(a+b)

# x = 1
# while x*x < n :
    # x += 1

# if x*x == n :
    # print('Yes')
# else :
    # print('No')
# '''
