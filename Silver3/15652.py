# N과 M (4)

"""
2021/08/12 11:04 오전
정웅교
문제: https://www.acmicpc.net/problem/15652
"""

n, m = map(int, input().split())
s = []


def f():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(1, n + 1):
        if len(s) > 0:
            if i < s[len(s) - 1]:
                continue
        s.append(i)
        f()
        s.pop()


f()
