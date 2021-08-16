# 합 구하기

"""
2021/08/16 1:01 오후
정웅교
문제: https://www.acmicpc.net/problem/11441
"""
from sys import stdin

n = int(stdin.readline())
ls1 = list(map(int, stdin.readline().split()))
ls = []
sum = 0
for i in ls1:
    sum += i
    ls.append(sum)
for _ in range(int(stdin.readline())):
    i, j = map(int, stdin.readline().split())
    i -= 2
    j -= 1
    if i < 0:
        print(ls[j])
    else:
        print(ls[j] - ls[i])
