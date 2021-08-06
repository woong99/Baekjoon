# 국영수

"""
2021/08/06 1:47 오후
정웅교
문제: https://www.acmicpc.net/problem/10825
"""
ls = []
for _ in range(int(input())):
    ls.append(list(map(str, input().split())))
s = sorted(ls, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for i in s:
    print(i[0])
