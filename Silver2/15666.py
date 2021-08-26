# N과 M (12)

"""
2021/08/26 3:41 오후
정웅교
문제: https://www.acmicpc.net/problem/15666
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
        if len(s) != 0:
            if ls[i] < s[len(s) - 1]:
                continue
        s.append(ls[i])
        last = ls[i]
        sol()
        s.pop()


sol()
