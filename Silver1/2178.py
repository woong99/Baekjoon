# 미로 탐색

"""
2022/01/08 12:57 오후
정웅교
문제: https://www.acmicpc.net/problem/2178
"""

import collections


def bfs():
    queue = collections.deque()
    queue.append([0, 0, 1])
    visited[0][0] = 1

    while queue:
        temp = queue.popleft()
        v1 = temp[0]
        v2 = temp[1]
        if v1 == n - 1 and v2 == m - 1:
            print(temp[2])
        for j in range(4):
            t1 = v1 + dx[j]
            t2 = v2 + dy[j]
            if 0 <= t1 < n and 0 <= t2 < m and visited[t1][t2] == 0 and graph[t1][t2] == '1':
                visited[t1][t2] = 1
                queue.append([t1, t2, temp[2] + 1])


n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited = [[0 for _ in range(m)] for _ in range(n)]
bfs()
