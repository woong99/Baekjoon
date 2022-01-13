# 현수막

"""
2022/01/13 7:46 오후
정웅교
문제: https://www.acmicpc.net/problem/14716
"""
import collections
import sys


def bfs(v1, v2):
    queue = collections.deque()
    queue.append([v1, v2])
    visited[v1][v2] = 1

    while queue:
        t1, t2 = queue.popleft()
        for j in range(8):
            if 0 <= t1 + dx[j] < m and 0 <= t2 + dy[j] < n and graph[t1 + dx[j]][t2 + dy[j]] == 1 and \
                    visited[t1 + dx[j]][
                        t2 + dy[j]] == 0:
                visited[t1 + dx[j]][t2 + dy[j]] = 1
                queue.append([t1 + dx[j], t2 + dy[j]])


m, n = map(int, sys.stdin.readline().split())
graph = []
dx = [1, -1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]
for _ in range(m):
    graph.append(list(map(int, sys.stdin.readline().split())))
visited = [[0 for _ in range(n)] for _ in range(m)]
cnt = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == 0:
            bfs(i, j)
            cnt += 1
print(cnt)
