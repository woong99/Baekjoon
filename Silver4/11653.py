# 소인수분해

"""
2021/07/11 3:40 오후
정웅교
문제: https://www.acmicpc.net/problem/11653
"""
from sys import stdin

n = int(stdin.readline())
if n == 1:
    exit()
k = 2
while n > 1:
    if n % k == 0:
        print(k)
        n = n // k
    else:
        k += 1
