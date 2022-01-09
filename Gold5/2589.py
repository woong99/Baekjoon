# 보물섬

"""
2022/01/09 11:16 오전
정웅교
문제: https://www.acmicpc.net/problem/2589
"""
import collections
import sys


def bfs(v1, v2):
    queue = collections.deque()
    queue.append([v1, v2, 0])
    visited[v1][v2] = 1

    while queue:
        temp = queue.popleft()
        v3 = temp[0]
        v4 = temp[1]
        for j in range(4):
            temp1 = v3 + dx[j]
            temp2 = v4 + dy[j]
            cnt = temp[2]
            if 0 <= temp1 < n and 0 <= temp2 < m and visited[temp1][temp2] == 0 and graph[temp1][temp2] == 'L':
                visited[temp1][temp2] = 1
                queue.append([temp1, temp2, cnt + 1])
    return cnt


n, m = map(int, sys.stdin.readline().split())
graph = []

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
for _ in range(n):
    graph.append(list(input()))

ls = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            visited = [[0 for _ in range(m)] for _ in range(n)]
            ls.append(bfs(i, j))
print(max(ls))
