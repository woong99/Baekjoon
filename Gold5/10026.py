# 적록색약

"""
2022/01/09 3:44 오후
정웅교
문제: https://www.acmicpc.net/problem/10026
"""
import collections


def bfs(v1, v2, color):
    queue = collections.deque()
    queue.append([v1, v2])
    visited[v1][v2] = 1
    while queue:
        temp = queue.popleft()
        v3 = temp[0]
        v4 = temp[1]
        for j in range(4):
            t3 = v3 + dx[j]
            t4 = v4 + dy[j]
            if 0 <= t3 < n and 0 <= t4 < n and visited[t3][t4] == 0 and graph[t3][t4] == color:
                visited[t3][t4] = 1
                queue.append([t3, t4])


n = int(input())
graph = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(n):
    graph.append(list(input()))
cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j, graph[i][j])
            cnt += 1
print(cnt, end=' ')
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'
cnt = 0
visited = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j, graph[i][j])
            cnt += 1
print(cnt)
