# 데스 나이트

"""
2022/01/12 11:47 오전
정웅교
문제: https://www.acmicpc.net/problem/16948
"""

import collections


def bfs(v1, v2):
    queue = collections.deque()
    queue.append([v1, v2])
    visited[v1][v2] = 0

    while queue:
        t1, t2 = queue.popleft()
        if t1 == r2 and t2 == c2:
            return visited[t1][t2]
            break
        for i in range(6):
            if 0 <= t1 + dx[i] < n and 0 <= t2 + dy[i] < n and visited[t1 + dx[i]][t2 + dy[i]] == 0:
                visited[t1 + dx[i]][t2 + dy[i]] = visited[t1][t2] + 1
                queue.append([t1 + dx[i], t2 + dy[i]])
    return -1


n = int(input())
r1, c1, r2, c2 = map(int, input().split())
visited = [[0 for _ in range(n)] for _ in range(n)]
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]
print(bfs(r1, c1))
