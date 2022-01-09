# DSLR

"""
2022/01/09 2:13 오후
정웅교
문제: https://www.acmicpc.net/problem/9019
"""
import collections
import sys


def bfs(v1, v2):
    visited = set()
    queue = collections.deque()
    queue.append([v1, ''])
    visited.add(v1)

    while queue:
        temp = queue.popleft()
        if temp[0] == v2:
            break

        for i in range(4):
            if i == 0:
                t1 = (temp[0] * 2) % 10000
                t2 = temp[1] + 'D'
            elif i == 1:
                if temp[0] == 0:
                    t1 = 9999
                else:
                    t1 = temp[0] - 1
                t2 = temp[1] + 'S'
            elif i == 2:
                t1 = (temp[0] % 1000) * 10 + (temp[0] // 1000)
                t2 = temp[1] + 'L'
            else:
                t1 = (temp[0] // 10) + ((temp[0] % 10) * 1000)
                t2 = temp[1] + 'R'
            if t1 not in visited:
                visited.add(t1)
                queue.append([t1, t2])
    return temp[1]


n = int(sys.stdin.readline())

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print(bfs(a, b))
