# 트리의 부모 찾기

"""
2021/08/18 1:06 오후
정웅교
문제: https://www.acmicpc.net/problem/11725
"""
import collections

n = int(input())
ls = [[0] * (n + 1) for i in range(n + 1)]
seen = [0] * (n + 1)
for _ in range(n - 1):
    a, b = map(int, input().split())
    ls[a][b] = ls[b][a] = 1

ls_res = [0 for i in range(n + 1)]


def bfs(v):
    queue = collections.deque()
    queue.append(v)
    seen[v] = 1

    while queue:
        v = queue.popleft()
        for i in range(1, n + 1):
            if ls[v][i] == 1 and seen[i] == 0:
                ls_res[i] = v
                queue.append(i)
                seen[i] = 1


bfs(1)
for i in range(2, len(ls_res)):
    print(ls_res[i])
