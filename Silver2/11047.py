# 동전 0

"""
2021/08/22 9:34 오후
정웅교
문제: https://www.acmicpc.net/problem/11047
"""

n, k = map(int, input().split())
ls = []
for _ in range(n):
    ls.append(int(input()))
cnt = 0
for i in range(len(ls) - 1, -1, -1):
    if ls[i] <= k:
        cnt += k // ls[i]
        k %= ls[i]
print(cnt)
