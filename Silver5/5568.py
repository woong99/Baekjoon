# 카드 놓기

"""
2021/06/28 11:50 오후
정웅교
문제: https://www.acmicpc.net/problem/5568
"""
import itertools

n = int(input())
k = int(input())
ls = []
s = set()
for _ in range(n):
    ls.append(input())
ls = list(itertools.permutations(ls, k))
for i in ls:
    p = ''
    for j in range(k):
        p += i[j]
    s.add(p)
print(len(s))
