# Circus

"""
2021/03/22 1:42 오후
정웅교
문제: https://www.acmicpc.net/problem/20352
"""
import math

n = int(input())
a = math.sqrt(n / math.pi)
print(round(2 * math.pi * a, 9))
