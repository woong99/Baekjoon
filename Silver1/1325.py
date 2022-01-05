# 효율적인 해킹

"""
2022/01/05 10:13 오후
정웅교
문제: https://www.acmicpc.net/problem/1325
"""

import collections
import sys


def bfs(j):
    visited = [0 for _ in range(n)]
    global cnt
    queue = collections.deque()
    queue.append(j)
    visited[j] = 1

    while queue:
        j = queue.popleft()
        cnt += 1
        for k in graph[j]:
            if visited[k] == 0:
                queue.append(k)
                visited[k] = 1


n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[b - 1].append(a - 1)
# for i in graph:
# print(i)
ls = []
max = 0
for i in range(n):
    cnt = 0
    if graph[i]:
        bfs(i)
        if cnt > max:
            max = cnt
            ls.clear()
            ls.append([i + 1, cnt])
        elif cnt == max:
            ls.append([i + 1, cnt])
ls.sort()
for i in ls:
    print(i[0], end=' ')
