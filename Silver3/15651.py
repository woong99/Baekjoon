# N과 M (3)

"""
2021/08/12 11:02 오전
정웅교
문제: https://www.acmicpc.net/problem/15651
"""

n, m = map(int, input().split())
s = []


def f():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(1, n + 1):
        s.append(i)
        f()
        s.pop()


f()
