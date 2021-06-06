# 달팽이는 올라가고 싶다

"""
2021/06/06 1:40 오후
정웅교
문제: https://www.acmicpc.net/problem/2869
"""
import math

a, b, v = map(int, input().split())
day = (v - b) / (a - b)
print(math.ceil(day))
