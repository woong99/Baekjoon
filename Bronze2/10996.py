# 별 찍기 - 21

"""
2021/05/20 1:40 오후
정웅교
문제: https://www.acmicpc.net/problem/10996
"""
import math

n = int(input())
if n == 1:
    print('*')
elif n == 2:
    print('*')
    print(' *')
    print('*')
    print(' *')
else:
    for i in range(n * 2):
        if i % 2 == 0:
            print('* ' * math.ceil(n / 2))
        elif i % 2 == 1:
            print(' *' * math.floor(n / 2))
