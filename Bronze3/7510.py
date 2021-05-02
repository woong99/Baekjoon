# 고급 수학

"""
2021/05/02 1:46 오후
정웅교
문제: https://www.acmicpc.net/problem/7510
"""
from sys import stdin

n = int(stdin.readline())
for i in range(1, n + 1):
    a, b, c = map(int, stdin.readline().split())
    ls = [a, b, c]
    ls.sort()
    if ls[0] ** 2 + ls[1] ** 2 == ls[2] ** 2:
        print(f"Scenario #{i}:")
        print('yes\n')
    else:
        print(f"Scenario #{i}:")
        print('no\n')
