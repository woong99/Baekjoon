# 별 찍기 - 7

"""
2021/03/31 2:02 오후
정웅교
문제: https://www.acmicpc.net/problem/2444
"""

n = int(input())
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))
for i in range(1, n):
    print(' ' * i + '*' * ((n - 1) * 2 - (2 * i - 1)))
