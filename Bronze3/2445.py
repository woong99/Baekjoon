# 별 찍기 - 8

"""
2021/03/31 2:05 오후
정웅교
문제: https://www.acmicpc.net/problem/2445
"""

n = int(input())
for i in range(1, n + 1):
    print('*' * i + ' ' * ((2 * n) - (i * 2)) + '*' * i)
for i in range(1, n):
    print('*' * (n - i) + ' ' * (2 * i) + '*' * (n - i))
