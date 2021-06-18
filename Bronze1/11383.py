# 뚊

"""
2021/06/19 4:41 오전
정웅교
문제: https://www.acmicpc.net/problem/11383
"""
a, b = map(int, input().split())
ls1 = []
ls2 = []
ls = []
for _ in range(a):
    ls1.append(list(input()))
for _ in range(a):
    ls2.append(input())
for k in range(a):
    s = ''
    for i in range(b):
        s += ls1[k][i] * 2
    ls.append(s)
if ls == ls2:
    print('Eyfa')
else:
    print('Not Eyfa')
