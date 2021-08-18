# 바이러스

"""
2021/08/18 11:43 오전
정웅교
문제: https://www.acmicpc.net/problem/2606
"""
n = int(input())
m = int(input())
ls = [[0] * (n + 1) for i in range(n + 1)]
seen = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    ls[a][b] = ls[b][a] = 1

cnt = 0


def dfs(v):
    global cnt
    seen[v] = 1
    for i in range(1, n + 1):
        if ls[v][i] == 1 and seen[i] == 0:
            dfs(i)
            cnt += 1


dfs(1)
print(cnt)
