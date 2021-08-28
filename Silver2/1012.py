# 유기농 배추

"""
2021/08/28 10:15 오전
정웅교
문제: https://www.acmicpc.net/problem/1012
"""
import sys

sys.setrecursionlimit(10000)


def search(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return
    if matrix[x][y] == 0:
        return
    matrix[x][y] = 0
    search(x, y + 1)
    search(x + 1, y)
    search(x - 1, y)
    search(x, y - 1)


for _ in range(int(input())):
    m, n, k = map(int, input().split())
    matrix = [[0] * m for i in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        matrix[b][a] = 1
    cnt = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                search(i, j)
                cnt += 1
    print(cnt)
