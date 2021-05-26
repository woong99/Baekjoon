# 카드 역배치

"""
2021/05/26 12:38 오후
정웅교
문제: https://www.acmicpc.net/problem/10804
"""
ls = list(range(1, 21))

for _ in range(10):
    a, b = map(int, input().split())
    ls1 = ls[a - 1: b]
    del ls[a - 1: b]
    ls1.reverse()
    for i in range(a - 1, b):
        ls.insert(i, ls1[i - (a - 1)])

for i in ls:
    print(i, end=' ')
