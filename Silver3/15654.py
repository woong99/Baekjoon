# N과 M (5)

"""
2021/08/12 11:09 오전
정웅교
문제: https://www.acmicpc.net/problem/15654
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
        if ls[i] in s:
            continue
        s.append(ls[i])
        f()
        s.pop()


f()
