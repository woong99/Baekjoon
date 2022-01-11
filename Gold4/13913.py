# 숨바꼭질 4

"""
2022/01/11 1:58 오후
정웅교
문제: https://www.acmicpc.net/problem/13913
"""
from collections import deque

n, m = map(int, input().split())
visited = [0] * 100001
path = []


def bfs(start, target):
    queue = deque()
    queue.append((start, 0))
    visited[start] = start
    while queue:
        temp, cnt = queue.popleft()
        # print(temp, cnt)
        if temp == target:
            idx = temp
            while idx != start:
                path.append(idx)
                idx = visited[idx]
            return cnt

        if 0 <= temp + 1 < 100001 and visited[temp + 1] == 0:
            queue.append((temp + 1, cnt + 1))
            visited[temp + 1] = temp
        if 0 <= temp - 1 < 100001 and visited[temp - 1] == 0:
            queue.append((temp - 1, cnt + 1))
            visited[temp - 1] = temp
        if 0 <= temp * 2 < 100001 and visited[temp * 2] == 0:
            queue.append((temp * 2, cnt + 1))
            visited[temp * 2] = temp


print(bfs(n, m))
path.append(n)
print(*path[::-1])
