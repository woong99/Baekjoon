# A -> B

"""
2022/01/12 11:27 오전
정웅교
문제: https://www.acmicpc.net/problem/16953
"""
import collections
import sys


def bfs(v1, v2):
    queue = collections.deque()
    queue.append([v1, 0])
    maximum = sys.maxsize
    while queue:
        t1, t2 = queue.popleft()
        if t1 == v2:
            maximum = min(t2, maximum)
        for i in range(2):
            if i == 0 and 1 <= t1 * 2 <= 10 ** 9:
                queue.append([t1 * 2, t2 + 1])
            elif i == 1 and 1 <= t1 * 10 + 1 <= 10 ** 9:
                queue.append([t1 * 10 + 1, t2 + 1])
    if maximum == sys.maxsize:
        return -1
    return maximum + 1


a, b = map(int, input().split())
print(bfs(a, b))
