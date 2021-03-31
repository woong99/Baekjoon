# 별 찍기 - 5

"""
2021/03/31 1:55 오후
정웅교
문제: https://www.acmicpc.net/problem/2442
"""

n = int(input())
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))
