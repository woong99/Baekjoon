# 연구소

"""
2022/01/10 11:01 오전
정웅교
문제: https://www.acmicpc.net/problem/14502
"""
import collections
import copy
import sys


def sol(i):
    if i == 3:
        visited2 = copy.deepcopy(visited)
        # for q in visited:
        #     print(q)
        # print()

        for v1 in range(n):
            for v2 in range(m):
                if visited[v1][v2] == '2':
                    bfs(v1, v2, visited2)
        cnt = 0
        for q in visited2:
            cnt += q.count('0')
        ls.append(cnt)
    else:
        for j in range(n):
            for k in range(m):
                if graph[j][k] == '0' and visited[j][k] == '0':
                    visited[j][k] = '1'
                    # graph[j][k] = '1'
                    sol(i + 1)
                    visited[j][k] = '0'
                    # graph[j][k] =


def bfs(t1, t2, v):
    visited1 = [[0 for _ in range(m)] for _ in range(n)]
    queue = collections.deque()
    queue.append([t1, t2])
    visited1[t1][t2] = 1

    while queue:
        temp1, temp2 = queue.popleft()
        for i in range(4):
            t3 = temp1 + dx[i]
            t4 = temp2 + dy[i]
            if 0 <= t3 < n and 0 <= t4 < m and v[t3][t4] == '0' and visited1[t3][t4] == 0:
                visited1[t3][t4] = 1
                v[t3][t4] = '2'
                queue.append([t3, t4])


n, m = map(int, sys.stdin.readline().split())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
graph = []

for _ in range(n):
    graph.append(list(input().split()))
visited = copy.deepcopy(graph)
# for j in graph:
#     print(j)
ls = []
sol(0)
print(max(ls))
