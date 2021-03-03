# 전자레인지

"""
2021/03/03 10:30 오전
정웅교
문제: https://www.acmicpc.net/problem/14470
"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
t = 0
status = 1
if a > 0:
    t = (b - a) * e
else:
    while 1:
        if a < 0:
            t += abs(a) * c
            a = 0
        elif a == 0 and status == 1:
            t += d
            status = 0
        elif a >= 0 and status == 0:
            t += b * e
            break
print(t)
