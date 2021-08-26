# N과 M (10)

"""
2021/08/26 3:02 오후
정웅교
문제: https://www.acmicpc.net/problem/15664
"""

n, m = map(int, input().split())
ls = list(map(int, input().split()))
ls.sort()
s = []
k = [False] * n


def sol():
    last = 0
    if len(s) == m:
        print(' '.join(map(str, s)))
    for i in range(n):
        if k[i] == True or last == ls[i]:
            continue
        if len(s) != 0:
            if ls[i] < s[len(s) - 1]:
                continue
        s.append(ls[i])
        k[i] = True
        last = ls[i]
        sol()
        s.pop()
        k[i] = False


sol()
