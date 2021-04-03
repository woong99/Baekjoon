# 이게 분수?

"""
2021/04/03 2:20 오후
정웅교
문제: https://www.acmicpc.net/problem/2863
"""

a, b = map(int, input().split())
c, d = map(int, input().split())
ls = []
for i in range(4):
    ls.append(a / c + b / d)
    temp = a
    a = c
    c = d
    d = b
    b = temp
k = max(ls)
cnt = 0
for i in range(4):
    if ls[i] == k:
        cnt += 1
if cnt == 1:
    print(ls.index(k))
else:
    print(min(ls))
