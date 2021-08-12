# N과 M (8)

"""
2021/08/12 11:18 오전
정웅교
문제: https://www.acmicpc.net/problem/15657
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
        if len(s) != 0:
            if ls[i] < s[len(s) - 1]:
                continue
        s.append(ls[i])
        f()
        s.pop()


f()
