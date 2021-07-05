# 피보나치 수 4

"""
2021/07/05 6:25 오후
정웅교
문제: https://www.acmicpc.net/problem/10826
"""


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    a = 0
    b = 1
    res = 0
    for i in range(2, n + 1):
        res = a + b
        a = b
        b = res
    return res


from sys import stdin

n = int(stdin.readline())
print(fib(n))
