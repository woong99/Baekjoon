# 별 찍기 - 6

"""
2021/03/31 2:00 오후
정웅교
문제: https://www.acmicpc.net/problem/2443
"""

n = int(input())
for i in range(1, n + 1):
    print(' ' * (i - 1) + '*' * (2 * n - (i * 2 - 1)))
