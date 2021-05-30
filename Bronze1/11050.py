# 이항 계수 1

"""
2021/05/30 10:39 오전
정웅교
문제: https://www.acmicpc.net/problem/11050
"""


def fac(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    return n * fac(n - 1)


n, k = map(int, input().split())
print(fac(n) // (fac(k) * fac(n - k)))
