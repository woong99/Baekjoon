# 소수 구하기

"""
2021/08/23 10:04 오전
정웅교
문제: https://www.acmicpc.net/problem/1929
"""
import math

m, n = map(int, input().split())


def isPrime(n):
    if n <= 1:
        return False
    if n % 2 == 0:
        if n == 2:
            return True
        return False
    for i in range(3, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


for i in range(m, n + 1):
    if isPrime(i):
        print(i)
