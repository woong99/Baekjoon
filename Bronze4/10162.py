# 전자레인지

"""
2021/02/27 10:25 오전
정웅교
문제: https://www.acmicpc.net/problem/10162
"""

n = int(input())
a, b, c = 0, 0, 0
if n >= 300:
    a = n // 300
    n = n % 300
else:
    a = 0
if n >= 60:
    b = n // 60
    n = n % 60
else:
    b = 0

if n % 10 != 0:
    print('-1')
else:
    if n >= 10:
        c = n // 10
        print(a, b, c)
    else:
        print(a, b, c)
