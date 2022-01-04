# 단지번호붙이기

"""
2022/01/03 2:12 오후
정웅교
문제: https://www.acmicpc.net/problem/2667
"""


def dfs(a, b, c):
    if a < 0 or b < 0 or a >= n or b >= n:
        return
    if graph[a][b] == '1':
        graph[a][b] = c
        dfs(a + 1, b, c)
        dfs(a, b + 1, c)
        dfs(a - 1, b, c)
        dfs(a, b - 1, c)


n = int(input())
graph = []
for _ in range(n):
    graph.append(list(input()))
    cnt = 2
for i in range(n):
    for j in range(n):
        if graph[i][j] == '1':
            dfs(i, j, cnt)
            cnt += 1

print(cnt - 2)
ls = []
for i in range(2, cnt):
    t = 0
    for j in graph:
        t += j.count(i)
    ls.append(t)
ls.sort()
for i in ls:
    print(i)
