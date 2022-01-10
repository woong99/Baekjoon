# 쉬운 최단거리

"""
2022/01/10 11:52 오전
정웅교
문제: https://www.acmicpc.net/problem/14940
"""
import collections
import sys


def bfs(v1, v2):
    queue = collections.deque()
    queue.append([v1, v2, 0])
    visited[v1][v2] = 1
    while queue:
        t1, t2, t3 = queue.popleft()
        ans[t1][t2] = t3

        for k in range(4):
            v3 = t1 + dx[k]
            v4 = t2 + dy[k]
            if 0 <= v3 < n and 0 <= v4 < m and visited[v3][v4] == 0:
                if graph[v3][v4] == '1':
                    visited[v3][v4] = 1

                    queue.append([v3, v4, t3 + 1])
                elif graph[v3][v4] == '0':
                    ans[v3][v4] = 0
                    visited[v3][v4] = 1


n, m = map(int, sys.stdin.readline().split())
graph = []
visited = [[0 for _ in range(m)] for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for _ in range(n):
    graph.append(list(input().split()))
ans = [[-1 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == '2':
            start = i
            end = j
bfs(start, end)
for i in range(n):
    for j in range(m):
        if graph[i][j] == '0':
            print(0, end=' ')
        else:
            print(ans[i][j], end=' ')
    print()
