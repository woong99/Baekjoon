# 경기 결과

"""
2021/05/01 11:01 오후
정웅교
문제: https://www.acmicpc.net/problem/5523
"""
from sys import stdin

n = int(stdin.readline())
cnt1 = 0
cnt2 = 0
for _ in range(n):
    a, b = map(int, stdin.readline().split())
    if a > b:
        cnt1 += 1
    elif a < b:
        cnt2 += 1
print(cnt1, cnt2)
