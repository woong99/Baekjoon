# 제로

"""
2021/07/01 11:47 오전
정웅교
문제: https://www.acmicpc.net/problem/10773
"""
from sys import stdin

ls = []
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    if n == 0:
        ls.pop()
    else:
        ls.append(n)
print(sum(ls))
