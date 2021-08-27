# 연결 요소의 개수

"""
2021/08/27 6:47 오후
정웅교
문제: https://www.acmicpc.net/problem/11724
"""
import sys

sys.setrecursionlimit(10000)
n, m = map(int, input().split())
matrix = [[0] * (n + 1) for i in range(n + 1)]
seen = [0] * (n + 1)
ls = [i for i in range(1, n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1


def dfs(v):
    seen[v] = 1
    for i in range(1, n + 1):
        if matrix[v][i] == 1 and seen[i] == 0:
            dfs(i)


cnt = 0
for i in range(1, n + 1):
    if seen[i] == 0:
        dfs(i)
        cnt += 1
print(cnt)
