# 두 수의 합

"""
2021/08/15 5:10 오후
정웅교
문제: https://www.acmicpc.net/problem/3273
"""
from sys import stdin

n = int(stdin.readline())
ls = list(map(int, stdin.readline().split()))
num = int(stdin.readline())
left, right = 0, len(ls) - 1
ls.sort()
cnt = 0
while left < right:
    tmp = ls[left] + ls[right]

    if tmp == num:
        cnt += 1
        left += 1
    elif tmp < num:
        left += 1
    else:
        right -= 1
print(cnt)
