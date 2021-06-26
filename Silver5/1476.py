# 날짜 계산

"""
2021/06/26 11:24 오후
정웅교
문제: https://www.acmicpc.net/problem/1476
"""
a, b, c = map(int, input().split())
d, e, f = 1, 1, 1
cnt = 1
while 1:
    if a == d and b == e and c == f:
        break
    d += 1
    e += 1
    f += 1
    cnt += 1
    if d == 16:
        d = 1
    if e == 29:
        e = 1
    if f == 20:
        f = 1

print(cnt)
