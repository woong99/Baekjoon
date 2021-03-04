# Winning Score

"""
2021/03/04 2:36 오후
정웅교
문제: https://www.acmicpc.net/problem/17009
"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
sum1 = a * 3 + b * 2 + c
sum2 = d * 3 + e * 2 + f
if sum1 > sum2:
    print('A')
elif sum1 < sum2:
    print('B')
else:
    print('T')
