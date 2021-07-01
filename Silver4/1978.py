# 소수 찾기

"""
2021/07/01 11:52 오전
정웅교
문제: https://www.acmicpc.net/problem/1978
"""

from math import sqrt
from sys import stdin


def sol(n):
    if n == '1':
        return False
    for i in range(2, int(sqrt(int(n))) + 1):
        if int(n) % i == 0:
            return False
    return True


n = int(stdin.readline())
ls = stdin.readline().split()
cnt = 0
for i in ls:
    if sol(i):
        cnt += 1
print(cnt)
