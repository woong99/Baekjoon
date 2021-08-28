# 섬의 개수

"""
2021/08/28 10:52 오전
정웅교
문제: https://www.acmicpc.net/problem/4963
"""
import sys

sys.setrecursionlimit(10000)


def search(x, y):
    if x < 0 or x >= h or y < 0 or y >= w:
        return
    if matrix[x][y] == 0:
        return
    matrix[x][y] = 0

    search(x + 1, y)
    search(x, y + 1)
    search(x - 1, y)
    search(x, y - 1)
    search(x - 1, y - 1)
    search(x - 1, y + 1)
    search(x + 1, y - 1)
    search(x + 1, y + 1)


while 1:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    matrix = []
    for _ in range(h):
        matrix.append(list(map(int, input().split())))
    cnt = 0
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 1:
                search(i, j)
                cnt += 1
    print(cnt)
