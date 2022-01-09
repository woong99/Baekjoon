# 숨바꼭질 2

"""
2022/01/09 4:05 오후
정웅교
문제: https://www.acmicpc.net/problem/12851
"""

import collections
import math
import sys


def bfs(v1, v2):
    cnt = 0
    minimum = math.inf
    queue = collections.deque()
    queue.append([v1, 0])
    visited[v1] = 1

    while queue:
        temp = queue.popleft()
        visited[temp[0]] = 1
        if temp[0] == v2:
            visited[temp[0]] = 0
            if temp[1] < minimum:
                cnt = 1
                minimum = temp[1]
            elif temp[1] == minimum:
                cnt += 1
        # else:
        #     if 0 <= temp[0] + 1 <= 100000 and visited[temp[0] + 1] == 0:
        #         queue.append([temp[0] + 1, temp[1] + 1])
        #     if 0 <= temp[0] - 1 <= 100000 and visited[temp[0] - 1] == 0:
        #         queue.append([temp[0] - 1, temp[1]])
        #     if 0 <= temp[0] * 2 <= 100000 and visited[temp[0] * 2] == 0:
        #         queue.append([temp[0] * 2, temp[1] + 1])
        else:
            for i in range(3):
                if i == 2:
                    t1 = temp[0] * 2
                else:
                    t1 = temp[0] + dx[i]
                if 0 <= t1 <= 100000 and visited[t1] == 0 and t1 <= 100000:
                    queue.append([t1, temp[1] + 1])
    return cnt, minimum


a, b = map(int, sys.stdin.readline().split())
dx = [1, -1, 2]
visited = [0 for _ in range(100001)]
ans = bfs(a, b)
print(ans[1])
print(ans[0])
