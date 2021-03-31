# 별 찍기 - 3

"""
2021/03/31 1:52 오후
정웅교
문제: https://www.acmicpc.net/problem/2440
"""

n = int(input())
for i in range(1, n + 1):
    print('*' * (n + 1 - i))
