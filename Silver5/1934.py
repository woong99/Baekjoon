# 최소공배수

"""
2021/06/20 2:30 오전
정웅교
문제: https://www.acmicpc.net/problem/1934
"""
import math

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(math.lcm(a, b))
