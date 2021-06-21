# 배열 합치기

"""
2021/06/21 6:09 오후
정웅교
문제: https://www.acmicpc.net/problem/11728
"""
a, b = map(int, input().split())
ls1 = list(map(int, input().split()))
ls2 = list(map(int, input().split()))
ls3 = ls1 + ls2
ls3.sort()
for i in ls3:
    print(i, end=' ')
