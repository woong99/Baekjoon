# 영역 구하기

"""
2022/01/04 3:22 오후
정웅교
문제: https://www.acmicpc.net/problem/2583
"""
import sys

sys.setrecursionlimit(10 ** 6)


def dfs(a, b, c):
    if a < 0 or a >= m or b < 0 or b >= n:
        return
    if graph[a][b] == 0:
        graph[a][b] = c
        dfs(a - 1, b, c)
        dfs(a, b - 1, c)
        dfs(a + 1, b, c)
        dfs(a, b + 1, c)


m, n, k = map(int, input().split())

graph = [[0 for _ in range(n)] for _ in range(m)]
for _ in range(k):
    a, b, c, d = map(int, input().split())
    for i in range(b, d):
        for j in range(a, c):
            graph[i][j] = 1
cnt = 2
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            dfs(i, j, cnt)
            cnt += 1

print(cnt - 2)
ls = []
for j in range(2, cnt):
    sum = 0
    for i in graph:
        sum += i.count(j)
    ls.append(sum)
ls.sort()
for i in ls:
    print(i, end=' ')
