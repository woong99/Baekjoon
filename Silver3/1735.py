# 분수 합

"""
2021/08/17 10:18 오전
정웅교
문제: https://www.acmicpc.net/problem/1735
"""

import math

a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
c = math.lcm(b1, b2)
c1 = c // b2
c2 = c // b1
d = a1 * c2 + a2 * c1
e = math.gcd(d, c)
print(d // e, c // e)
