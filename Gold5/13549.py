# 숨바꼭질 3

"""
2022/01/10 10:26 오전
정웅교
문제: https://www.acmicpc.net/problem/13549
"""
import collections
import sys


def bfs(v1, v2):
    queue = collections.deque()
    queue.append([v1, 0])
    visited[v1] = 1
    min_cnt = sys.maxsize

    while queue:
        temp = queue.popleft()
        if temp[0] == v2:
            visited[temp[0]] = 0
            min_cnt = min(min_cnt, temp[1])

        if 0 <= temp[0] + 1 <= 100000 and visited[temp[0] + 1] == 0:
            visited[temp[0] + 1] = 1
            queue.append([temp[0] + 1, temp[1] + 1])
        if 0 <= temp[0] * 2 <= 100000 and visited[temp[0] * 2] == 0:
            visited[temp[0] * 2] = 1
            queue.append([temp[0] * 2, temp[1]])
        if 0 <= temp[0] - 1 <= 100000 and visited[temp[0] - 1] == 0:
            visited[temp[0] - 1] = 1
            queue.append([temp[0] - 1, temp[1] + 1])
    return min_cnt


n, m = map(int, sys.stdin.readline().split())
visited = [0 for _ in range(100001)]
print(bfs(n, m))
