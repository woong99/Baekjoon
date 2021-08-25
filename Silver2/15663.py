# N과 M (9)

"""
2021/08/25 3:43 오후
정웅교
문제: https://www.acmicpc.net/problem/15663
"""
from sys import stdin

n, m = map(int, stdin.readline().split())
ls = list(map(int, stdin.readline().split()))
ls.sort()
ls1 = []
ls2 = []
visited = [False] * n


def sol():
    if len(ls1) == m:
        print(' '.join(map(str, ls1)))
        return
    last = 0
    for i in range(len(ls)):
        if visited[i] or last == ls[i]:
            continue
        ls1.append(ls[i])
        last = ls[i]
        visited[i] = True
        sol()
        visited[i] = False
        ls1.pop()


sol()
