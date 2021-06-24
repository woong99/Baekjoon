# 최대 GCD

"""
2021/06/24 10:23 오후
정웅교
문제: https://www.acmicpc.net/problem/9417
"""
import itertools
import math

for _ in range(int(input())):
    ls = list(map(int, input().split()))
    s = list(itertools.combinations(ls, 2))
    ls1 = []
    for k in range(len(s)):
        ls1.append(math.gcd(s[k][0], s[k][1]))
    print(max(ls1))
