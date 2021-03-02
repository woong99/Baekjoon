# 베시와 데이지

"""
2021/03/02 6:24 오후
정웅교
문제: https://www.acmicpc.net/problem/16431
"""

b1, b2 = map(int, input().split())
d1, d2 = map(int, input().split())
j1, j2 = map(int, input().split())

b = [abs(b1 - j1), abs(b2 - j2)]
d = [abs(d1 - j1), abs(d2 - j2)]
b_cnt = sum(b) - min(b)
d_cnt = sum(d)
if b_cnt < d_cnt:
    print('bessie')
elif b_cnt > d_cnt:
    print('daisy')
else:
    print('tie')
