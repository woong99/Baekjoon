# 현명한 나이트

"""
2022/01/12 11:57 오전
정웅교
문제: https://www.acmicpc.net/problem/18404
"""
import collections
import sys


def bfs(v1, v2):
    queue = collections.deque()
    queue.append([v1, v2])
    visited[v1][v2] = 0
    while queue:
        t1, t2 = queue.popleft()
        for i in range(8):
            if 0 <= t1 + dx[i] < n and 0 <= t2 + dy[i] < n and visited[t1 + dx[i]][t2 + dy[i]] == 0:
                visited[t1 + dx[i]][t2 + dy[i]] = visited[t1][t2] + 1
                queue.append([t1 + dx[i], t2 + dy[i]])


n, m = map(int, sys.stdin.readline().split())
visited = [[0 for _ in range(n)] for _ in range(n)]
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]
x, y = map(int, sys.stdin.readline().split())
bfs(x - 1, y - 1)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(visited[a - 1][b - 1], end=' ')
