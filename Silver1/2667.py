# 단지번호붙이기

"""
2022/01/03 2:12 오후
정웅교
문제: https://www.acmicpc.net/problem/2667
"""


def dfs(a, b):
    if a < 0 or b < 0 or a >= n or b >= n or graph[a][b] == 0:
        return
    visited[a][b] = 1
    dfs(a + 1, b)
    dfs(a, b + 1)
    dfs(a - 1, b)
    dfs(a, b - 1)


n = int(input())
# graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
graph = []
visited = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(n):
    s = list(input())
    ls = []
    for i in s:
        ls.append(int(i))
    graph.append(ls)

for i in graph:
    print(i)
print()

dfs(0, 1)
for i in visited:
    print(i)
