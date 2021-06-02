# 행렬 덧셈

"""
2021/06/02 1:24 오후
정웅교
문제: https://www.acmicpc.net/problem/2738
"""
n, m = map(int, input().split())
a, b = [], []
for i in [a, b]:
    for j in range(n):
        i.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        a[i][j] += b[i][j]
    print(*a[i])
