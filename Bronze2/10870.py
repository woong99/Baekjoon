# 피보나치 수 5

"""
2021/05/18 11:40 오후
정웅교
문제: https://www.acmicpc.net/problem/10870
"""


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    pp = 0
    p = 1
    result = 0

    for i in range(2, n + 1):
        result = p + pp
        pp = p
        p = result
    return result


n = int(input())
print(fib(n))
