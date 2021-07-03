# 통계학

"""
2021/07/03 8:35 오후
정웅교
문제: https://www.acmicpc.net/problem/2108
"""
from collections import Counter
from sys import stdin

ls = []
n = int(stdin.readline())
for _ in range(n):
    ls.append(int(stdin.readline()))
ls.sort()
print(round(sum(ls) / n))
print(ls[len(ls) // 2])
ct = Counter(ls)
k = ct.most_common()
p = k[0][1]
s = k[0][0]
if len(k) != 1:
    if k[1][1] == p:
        s = k[1][0]
print(s)
print(max(ls) - min(ls))
