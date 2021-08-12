# N과 M (7)

"""
2021/08/12 11:18 오전
정웅교
문제: https://www.acmicpc.net/problem/15656
"""

n, m = map(int, input().split())
ls = list(map(int, input().split()))
ls.sort()
s = []


def f():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(n):
        s.append(ls[i])
        f()
        s.pop()


f()
