# 블랙잭

"""
2021/05/18 11:14 오후
정웅교
문제: https://www.acmicpc.net/problem/2798
"""
import itertools

n, m = map(int, input().split())
ls = list(map(int, input().split()))
ncr = itertools.combinations(ls, 3)
ls1 = list(ncr)
ls2 = []
for i in range(len(ls1)):
    ls2.append(sum(ls1[i]))
ls2.sort()
a = 0
for i in range(len(ls2)):
    if ls2[i] > m:
        break
    else:
        a = ls2[i]
print(a)
