# 노드사이의 거리

"""
2022/01/09 10:41 오전
정웅교
문제: https://www.acmicpc.net/problem/1240
"""
import collections
import sys


def bfs(v1, v2):
    queue = collections.deque()
    queue.append([v1, 0])
    visited[v1] = 1

    while queue:
        temp = queue.popleft()
        v3 = temp[0]
        v4 = temp[1]
        if v3 == v2:
            break
        for j in range(n):
            if graph[v3][j] != 0 and visited[j] == 0:
                visited[j] = 1
                queue.append([j, v4 + graph[v3][j]])
    return v4


n, m = map(int, sys.stdin.readline().split())
graph = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(n - 1):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a - 1][b - 1], graph[b - 1][a - 1] = c, c

for _ in range(m):
    d, e = map(int, sys.stdin.readline().split())
    visited = [0 for _ in range(n)]
    print(bfs(d - 1, e - 1))
