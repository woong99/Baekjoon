# 쉽게 푸는 문제

"""
2021/06/22 6:07 오후
정웅교
문제: https://www.acmicpc.net/problem/1292
"""
ls = []
a, b = map(int, input().split())
k = 1
cnt = 0
for i in range(b):
    if cnt == k:
        k += 1
        cnt = 0
    ls.append(k)
    cnt += 1
print(sum(ls[a - 1:b]))
