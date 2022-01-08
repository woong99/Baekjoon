# 나이트의 이동

"""
2022/01/08 10:11 오전
정웅교
문제: https://www.acmicpc.net/problem/7562
"""
import collections


def bfs(v1, v2):
    queue = collections.deque()
    queue.append([v1, v2, 0])
    visited[v1][v2] = 1

    while queue:
        temp = queue.popleft()
        v1 = temp[0]
        v2 = temp[1]
        v3 = temp[2]
        if v1 == c and v2 == d:
            print(v3)
            break
        for j in range(8):
            temp1 = v1 + ls[j][0]
            temp2 = v2 + ls[j][1]
            if 0 <= temp1 < n and 0 <= temp2 < n:
                if visited[temp1][temp2] == 0:
                    visited[temp1][temp2] = 1
                    queue.append([temp1, temp2, v3 + 1])


m = int(input())
for _ in range(m):
    n = int(input())
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    ls = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]
    visited = [[0 for _ in range(n)] for _ in range(n)]
    if a == c and b == d:
        print(0)
    else:
        bfs(a, b)
