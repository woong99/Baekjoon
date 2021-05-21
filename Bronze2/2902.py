# KMP는 왜 KMP일까?

"""
2021/05/21 1:11 오후
정웅교
문제: https://www.acmicpc.net/problem/2902
"""
s = str(input())
ls = s.split('-')
res = []
for i in ls:
    res.append(i[0])
for k in res:
    print(k, end='')
