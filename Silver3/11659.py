# 구간 합 구하기 4

"""
2021/08/15 11:06 오전
정웅교
문제: https://www.acmicpc.net/problem/11659
"""
from sys import stdin

n, m = map(int, stdin.readline().split())
ls = list(map(int, stdin.readline().split()))
ls1 = []
sum = 0
for i in range(len(ls)):
    sum += ls[i]
    ls1.append(sum)
for _ in range(m):
    i, j = map(int, stdin.readline().split())
    if i - 1 == 0:
        print(ls1[j - 1])
    else:
        print(ls1[j - 1] - ls1[i - 2])
