# 스타트링크

"""
2022/01/09 1:52 오후
정웅교
문제: https://www.acmicpc.net/problem/5014
"""
import collections
import sys


def bfs(v1, v2):
    stat = False
    queue = collections.deque()
    queue.append([v1, 0])
    visited[v1] = 1

    while queue:
        temp = queue.popleft()
        if temp[0] == v2:
            stat = True
            break
        for j in range(2):
            t = temp[0] + dx[j]
            if 0 <= t < f and visited[t] == 0:
                visited[t] = 1
                queue.append([t, temp[1] + 1])
    return temp[1], stat


f, s, g, u, d = map(int, sys.stdin.readline().split())
visited = [0 for _ in range(f)]
dx = [u, -d]
sol = bfs(s - 1, g - 1)
if sol[1]:
    print(sol[0])
else:
    print('use the stairs')
