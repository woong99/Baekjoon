# 적어도 대부분의 배수

"""
2021/06/17 5:07 오후
정웅교
문제: https://www.acmicpc.net/problem/1145
"""
from itertools import combinations
from math import lcm


def sol(a, b, c):
    n = lcm(a, b)
    return lcm(n, c)


ls = list(map(int, input().split()))

ls1 = list(combinations(ls, 3))
ls3 = []
for i in ls1:
    ls2 = list(i)
    ls3.append(sol(ls2[0], ls2[1], ls2[2]))
print(min(ls3))
