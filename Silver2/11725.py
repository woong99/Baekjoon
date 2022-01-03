# 트리의 부모 찾기

"""
2022/01/03 1:25 오후
정웅교
문제: https://www.acmicpc.net/problem/11725
"""

import sys

sys.setrecursionlimit(10 ** 9)


def dfs(v):
    for i in ls[v]:
        if seen[i] == 0:
            seen[i] = v
            dfs(i)


n = int(input())
ls = [[] for i in range(n + 1)]
seen = [0] * (n + 1)
ans = [0] * (n + 1)
for _ in range(n - 1):
    a, b = map(int, input().split())
    ls[a].append(b)
    ls[b].append(a)
seen[1] = -1
dfs(1)
for k in seen[2:]:
    print(k)
