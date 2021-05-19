# 일곱 난쟁이

"""
2021/05/19 2:21 오후
정웅교
문제: https://www.acmicpc.net/problem/2309
"""
import itertools

ls = list()
for _ in range(9):
    ls.append(int(input()))
combi = itertools.combinations(ls, 7)
ls1 = list(combi)
for i in range(len(ls1)):
    if sum(ls1[i]) == 100:
        a = sorted(list(ls1[i]))
for i in a:
    print(i)
