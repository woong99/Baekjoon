# 별 찍기 - 12

"""
2021/04/01 1:25 오후
정웅교
문제: https://www.acmicpc.net/problem/2522
"""

n = int(input())
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * i)
for i in range(1, n):
    print(' ' * i + '*' * (n - i))
