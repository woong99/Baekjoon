# 쿠폰

"""
2021/03/01 4:52 오후
정웅교
문제: https://www.acmicpc.net/problem/10179
"""

n = int(input())
ls = []
for i in range(n):
    k = float(input())
    ls.append(k)
for i in range(n):
    print('$' + format(ls[i] * 0.8, ".2f"))
