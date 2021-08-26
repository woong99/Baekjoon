# N과 M (11)

"""
2021/08/26 3:15 오후
정웅교
문제: https://www.acmicpc.net/problem/15665
"""

n, m = map(int, input().split())
ls = list(map(int, input().split()))
ls.sort()
s = []


def sol():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    last = 0
    for i in range(n):
        if last == ls[i]:
            continue
        s.append(ls[i])
        last = ls[i]
        sol()
        s.pop()


sol()
