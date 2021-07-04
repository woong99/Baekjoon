# 피보나치 수

"""
2021/07/04 9:25 오후
정웅교
문제: https://www.acmicpc.net/problem/4150
"""


def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    pp = 0
    p = 1
    res = 0

    for i in range(2, n + 1):
        res = p + pp
        pp = p
        p = res
    return res


n = int(input())
print(fib(n))
