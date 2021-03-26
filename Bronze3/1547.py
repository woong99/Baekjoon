# 공

"""
2021/03/26 5:56 오후
정웅교
문제: https://www.acmicpc.net/problem/1547
"""

m = int(input())
k = 1
ls = [1, 2, 3]
for i in range(m):
    a, b = map(int, input().split())

    xi = ls.index(a)
    yi = ls.index(b)
    ls[xi], ls[yi] = ls[yi], ls[xi]
print(ls[0])
