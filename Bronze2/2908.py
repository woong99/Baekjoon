# 상수

"""
2021/05/17 4:35 오후
정웅교
문제: https://www.acmicpc.net/problem/2908
"""

a, b = map(str, input().split())
c = int(a[::-1])
d = int(b[::-1])
if c > d:
    print(c)
else:
    print(d)
