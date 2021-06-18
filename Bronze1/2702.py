# 초6 수학

"""
2021/06/18 11:45 오후
정웅교
문제: https://www.acmicpc.net/problem/2702
"""
import math

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(math.lcm(a, b), math.gcd(a, b))
