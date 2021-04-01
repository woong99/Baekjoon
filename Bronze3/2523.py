# 별 찍기 - 13

"""
2021/04/01 1:27 오후
정웅교
문제: https://www.acmicpc.net/problem/2523
"""

n = int(input())
for i in range(1, n + 1):
    print('*' * i)
for i in range(1, n):
    print('*' * (n - i))
