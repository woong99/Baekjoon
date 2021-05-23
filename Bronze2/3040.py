# 백설 공주와 일곱 난쟁이

"""
2021/05/23 3:03 오후
정웅교
문제: https://www.acmicpc.net/problem/3040
"""
import itertools

ls = []
for _ in range(9):
    ls.append(int(input()))
ls1 = itertools.combinations(ls, 7)
ls1 = list(ls1)
for i in ls1:
    if sum(i) == 100:
        for k in i:
            print(k)
