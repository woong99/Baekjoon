# N과 M (1)

"""
2021/08/12 9:52 오전
정웅교
문제: https://www.acmicpc.net/problem/15649
"""


def dfs(v):
    if len(s) == m:
        print(*s)
    for i in range(1, n + 1):
        s.append(i)
        dfs(i)
        s.pop()


n, m = map(int, input().split())
visited = [0 for _ in range(n)]
s = []
dfs(1)
