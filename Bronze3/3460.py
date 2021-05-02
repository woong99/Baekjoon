# 이진수

"""
2021/05/02 1:49 오후
정웅교
문제: https://www.acmicpc.net/problem/3460
"""
from sys import stdin

n = int(stdin.readline())
for _ in range(n):
    a = int(stdin.readline())
    k = str(bin(a))
    for i in range(len(k) - 1, 1, -1):
        if k[i] == '1':
            print(len(k) - 1 - i, end=" ")
