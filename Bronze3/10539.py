# 수빈이와 수열

"""
2021/05/16 4:33 오후
정웅교
문제: https://www.acmicpc.net/problem/10539
"""

n = int(input())
ls = list(map(int, input().split()))
ls1 = []
ls1.append(ls[0])
for i in range(1, len(ls)):
    ls1.append((i + 1) * ls[i] - sum(ls1))
for i in ls1:
    print(i, end=' ')
