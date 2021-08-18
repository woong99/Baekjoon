# DFS와 BFS

"""
2021/08/18 11:10 오전
정웅교
문제: https://www.acmicpc.net/problem/1260
"""
import collections

n, m, v = map(int, input().split())
matrix = [[0] * (n + 1) for i in range(n + 1)]
seen = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1


def dfs(v):
    seen[v] = 1
    print(v, end=' ')
    for i in range(1, n + 1):
        if matrix[v][i] == 1 and seen[i] == 0:
            dfs(i)


def bfs(v):
    queue = collections.deque()
    queue.append(v)
    seen[v] = 1

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, n + 1):
            if matrix[v][i] == 1 and seen[i] == 0:
                queue.append(i)
                seen[i] = 1


dfs(v)
seen = [0] * (n + 1)
print()
bfs(v)
