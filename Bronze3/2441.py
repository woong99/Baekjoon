# 별 찍기 - 4

"""
2021/03/31 1:53 오후
정웅교
문제: https://www.acmicpc.net/problem/2441
"""

n = int(input())
for i in range(1, n + 1):
    print(' ' * (i - 1) + '*' * (n + 1 - i))
