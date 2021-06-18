# 반올림

"""
2021/06/19 3:54 오전
정웅교
문제: https://www.acmicpc.net/problem/2033
"""

n = int(input())
d = 10
while n > d:
    if n % d >= d // 2:
        n += d
    n -= (n % d)
    d *= 10
print(n)
