# 숫자 카드 2

"""
2021/07/20 11:56 오전
정웅교
문제: https://www.acmicpc.net/problem/10816
"""
from collections import Counter
from sys import stdin

a = int(stdin.readline())
ls1 = list(map(int, input().split()))
ls2 = Counter(ls1)
ls4 = set(ls1)
b = int(stdin.readline())
ls3 = list(map(int, input().split()))
for i in ls3:
    if i in ls4:
        print(ls2.get(i), end=' ')
    else:
        print(0, end=' ')
