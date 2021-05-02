# 팩토리얼 진법

"""
2021/05/02 11:14 오전
정웅교
문제: https://www.acmicpc.net/problem/5692
"""
from sys import stdin


def fac(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result


while 1:
    n = int(stdin.readline())
    if n == 0:
        break
    result = 0
    for i in range(len(str(n))):
        result = result + ((n % 10) * fac(i + 1))
        n = n // 10
    print(result)
