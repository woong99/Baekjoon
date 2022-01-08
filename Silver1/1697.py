# 숨바꼭질

"""
2022/01/08 1:19 오후
정웅교
문제: https://www.acmicpc.net/problem/1697
"""

import collections


def bfs():
    queue = collections.deque()
    queue.append([n, 0])
    visited[n] = 1

    while queue:
        temp = queue.popleft()
        if temp[0] == k:
            print(temp[1])
            break
        for i in range(3):
            if dx[i] == 2:
                v = temp[0] * 2
            else:
                v = temp[0] + dx[i]
            if 0 <= v <= 100000 and visited[v] == 0:
                visited[v] = 1
                queue.append([v, temp[1] + 1])


n, k = map(int, input().split())
visited = [0 for _ in range(1000000)]
dx = [-1, 1, 2]
bfs()
