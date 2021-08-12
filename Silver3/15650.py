# N과 M (2)

"""
2021/08/12 10:46 오전
정웅교
문제: https://www.acmicpc.net/problem/15650
"""

n, m = map(int, input().split())
s = []


def f():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(1, n + 1):
        if i in s:
            continue
        if len(s) > 0:
            if i < s[len(s) - 1]:
                continue
        s.append(i)
        f()
        s.pop()


f()
