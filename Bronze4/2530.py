# 인공지능 시계

"""
2021/02/27 10:10 오전
정웅교
문제: https://www.acmicpc.net/problem/2530
"""

a, b, c = map(int, input().split())
n = int(input())
if c + n >= 60:
    b += (c + n) // 60
    c = (c + n) % 60
    if b >= 60:
        a += b // 60
        b = b % 60

    if a >= 24:
        a = a % 24
else:
    c += n
print(a, b, c)
