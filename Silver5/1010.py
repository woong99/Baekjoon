# 다리 놓기

"""
2021/06/20 11:45 오후
정웅교
문제: https://www.acmicpc.net/problem/1010
"""


def fac(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    sum = 1
    for i in range(2, n + 1):
        sum *= i
    return sum


def nCr(a, b):
    res = fac(b) // (fac(a) * fac(b - a))
    return res


for _ in range(int(input())):
    a, b = map(int, input().split())
    print(nCr(a, b))
