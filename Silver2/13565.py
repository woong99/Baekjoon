# 침투

"""
2022/01/04 2:34 오후
정웅교
문제: https://www.acmicpc.net/problem/13565
"""
import sys

sys.setrecursionlimit(10 ** 6)


def dfs(a, b):
    if a < 0 or a >= m or b < 0 or b >= n:
        return
    if graph[a][b] == '0':
        graph[a][b] = '2'
        dfs(a - 1, b)
        dfs(a, b - 1)
        dfs(a + 1, b)
        dfs(a, b + 1)


m, n = map(int, input().split())
graph = []
for _ in range(m):
    graph.append(list(input()))
for i in range(n):
    dfs(0, i)
if '2' in graph[m - 1]:
    print('YES')
else:
    print('NO')
