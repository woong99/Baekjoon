# 별 찍기 - 2

"""
2021/03/31 1:49 오후
정웅교
문제: https://www.acmicpc.net/problem/2439
"""
n = int(input())
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * i)
