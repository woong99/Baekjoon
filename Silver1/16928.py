# 뱀과 사다리 게임

"""
2022/01/13 7:59 오후
정웅교
문제: https://www.acmicpc.net/problem/16928
"""
import collections
import sys


def bfs():
    queue = collections.deque()
    queue.append([1, 0])
    visited[1] = 1

    while queue:
        t, cnt = queue.popleft()
        if t == 100:
            print(cnt)
            break
        for i in range(1, 7):
            if t + i < 101 and visited[t + i] == 0:
                if t + i in a1:
                    for j in range(n):
                        if a1[j] == t + i:
                            visited[a2[j]] = 1
                            queue.append([a2[j], cnt + 1])
                elif t + i in b1:
                    for j in range(m):
                        if b1[j] == t + i:
                            visited[b2[j]] = 1
                            queue.append([b2[j], cnt + 1])
                else:
                    visited[t + i] = 1
                    queue.append([t + i, cnt + 1])


n, m = map(int, sys.stdin.readline().split())
visited = [0 for _ in range(102)]
a1 = []
a2 = []
b1 = []
b2 = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    a1.append(x)
    a2.append(y)
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    b1.append(u)
    b2.append(v)
bfs()
