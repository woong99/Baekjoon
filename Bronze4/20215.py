# Cutting Corners

"""
2021/03/22 1:50 오후
정웅교
문제: https://www.acmicpc.net/problem/20215
"""
import math

w, h = map(int, input().split())
print(round(w + h - math.sqrt(w ** 2 + h ** 2), 9))
