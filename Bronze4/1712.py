# 손익분기점

"""
2021/02/25 10:03 오후
정웅교
문제: https://www.acmicpc.net/problem/1712
"""

a, b, c = map(int, input().split())

if b < c:
    print(a // (c - b) + 1)
else:
    print('-1')
