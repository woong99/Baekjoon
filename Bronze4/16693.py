# Pizza Deal

"""
2021/03/16 2:53 오후
정웅교
문제: https://www.acmicpc.net/problem/16693
"""
import math

a1, p1 = map(int, input().split())
r1, p2 = map(int, input().split())

n1 = a1 / p1
n2 = (r1 ** 2) * math.pi / p2
if n1 < n2:
    print('Whole pizza')
else:
    print('Slice of pizza')
