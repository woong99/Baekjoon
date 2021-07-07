# 이진수 덧셈

"""
2021/07/07 2:03 오후
정웅교
문제: https://www.acmicpc.net/problem/2729
"""
from sys import stdin

for _ in range(int(stdin.readline())):
    a, b = map(str, input().split())
    s = int(a, 2) + int(b, 2)
    print(bin(s)[2:])
