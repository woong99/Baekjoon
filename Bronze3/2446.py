# 별 찍기 - 9

"""
2021/03/31 2:08 오후
정웅교
문제: https://www.acmicpc.net/problem/2446
"""

n = int(input())
for i in range(1, n + 1):
    print(' ' * (i - 1) + '*' * (2 * n - (2 * i - 1)))
for i in range(1, n):
    print(' ' * (n - 1 - i) + '*' * (2 * i + 1))
