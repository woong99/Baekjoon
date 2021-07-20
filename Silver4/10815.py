# 숫자 카드

"""
2021/07/20 11:46 오전
정웅교
문제: https://www.acmicpc.net/problem/10815
"""
from sys import stdin

a = int(stdin.readline())
ls1 = set(map(int, input().split()))
b = int(stdin.readline())
ls2 = list(map(int, input().split()))
for i in ls2:
    if i in ls1:
        print(1, end=' ')
    else:
        print(0, end=' ')
