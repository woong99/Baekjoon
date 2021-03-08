# 헛간 청약

"""
2021/03/08 2:55 오후
정웅교
문제: https://www.acmicpc.net/problem/19698
"""

a, b, c, d = map(int, input().split())
n = (b // d) * (c // d)
if n > a:
    print(a)
else:
    print(n)
