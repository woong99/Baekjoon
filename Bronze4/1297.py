# TV 크기

"""
2021/02/28 5:20 오후
정웅교
문제: https://www.acmicpc.net/problem/1297
"""
import math

a, b, c = map(int, input().split())
n1 = math.sqrt(a ** 2 / (b ** 2 + c ** 2))
print(int(n1 * b), int(n1 * c))
