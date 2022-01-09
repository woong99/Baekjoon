# 치즈

"""
2022/01/09 12:19 오후
정웅교
문제: https://www.acmicpc.net/problem/2636
"""
import collections


def bfs():
    queue = collections.deque()
    queue.append([0, 0])
    visited[0][0] = 1

    while queue:
        temp = queue.popleft()
        v1 = temp[0]
        v2 = temp[1]
        for j in range(4):
            t1 = v1 + dx[j]
            t2 = v2 + dy[j]
            if 0 <= t1 < n and 0 <= t2 < m and visited[t1][t2] == 0:
                visited[t1][t2] = 1
                if graph[t1][t2] == '1':
                    graph[t1][t2] = '0'
                else:
                    queue.append([t1, t2])


n, m = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
graph = []
visited = [[0 for _ in range(m)] for _ in range(n)]
for _ in range(n):
    graph.append(list(input().split()))
ls = []
c = 0
while 1:
    cnt = 0
    for i in graph:
        for j in i:
            if j == '1':
                cnt += 1
    ls.append(cnt)
    if cnt == 0:
        break
    bfs()
    c += 1
    visited = [[0 for _ in range(m)] for _ in range(n)]
print(c)
print(ls[c - 1])
