# 카드2

"""
2021/07/20 11:15 오전
정웅교
문제: https://www.acmicpc.net/problem/2164
"""
from collections import deque
from sys import stdin

n = int(stdin.readline())
ls = deque([i for i in range(n, 0, -1)])
while len(ls) > 1:
    ls.pop()
    a = ls.pop()
    ls.appendleft(a)
print(ls[0])
