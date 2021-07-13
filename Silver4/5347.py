# LCM

"""
2021/07/13 10:20 오전
정웅교
문제: https://www.acmicpc.net/problem/5347
"""
import math
from sys import stdin

for _ in range(int(stdin.readline())):
    a, b = map(int, input().split())
    print(math.lcm(a, b))
