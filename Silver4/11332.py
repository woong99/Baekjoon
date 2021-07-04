# 시간초과

"""
2021/07/04 9:34 오후
정웅교
문제: https://www.acmicpc.net/problem/11332
"""
import math
from sys import stdin

for _ in range(int(stdin.readline())):
    a, b, c, d = map(str, input().split())
    if a == 'O(N)':
        sum = int(b) * int(c)
        if sum <= int(d) * 100000000:
            print('May Pass.')
        else:
            print('TLE!')
    elif a == 'O(2^N)':
        sum = 2 ** int(b) * int(c)
        if sum <= int(d) * 100000000:
            print('May Pass.')
        else:
            print('TLE!')
    elif a == 'O(N!)':
        sum = math.factorial(int(b)) * int(c)
        if sum <= int(d) * 100000000:
            print('May Pass.')
        else:
            print('TLE!')
    elif a == 'O(N^2)':
        sum = int(b) ** 2 * int(c)
        if sum <= int(d) * 100000000:
            print('May Pass.')
        else:
            print('TLE!')
    elif a == 'O(N^3)':
        sum = int(b) ** 3 * int(c)
        if sum <= int(d) * 100000000:
            print('May Pass.')
        else:
            print('TLE!')
