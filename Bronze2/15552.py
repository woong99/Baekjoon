# 빠른 A+B

"""
2021/05/17 1:17 오전
정웅교
문제: https://www.acmicpc.net/problem/15552
"""

from sys import stdin

n = int(stdin.readline())
for _ in range(n):
    a, b = map(int, stdin.readline().split())
    print(a + b)
