# 스캐너

"""
2021/06/19 4:09 오전
정웅교
문제: https://www.acmicpc.net/problem/3035
"""
r, c, zr, zc = map(int, input().split())
ls = []
ls1 = []
for _ in range(r):
    ls.append(input())
for k in ls:
    ls3 = []
    for i in k:
        for _ in range(zc):
            ls3.append(i)

    s = ''.join(ls3)
    ls1.append(s)
for i in range(r):
    for k in range(zr):
        print(ls1[i])
