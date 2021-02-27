# 방학 숙제

"""
2021/02/27 10:36 오전
정웅교
문제: https://www.acmicpc.net/problem/5532
"""

l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

while 1:
    a -= c
    b -= d
    l -= 1
    if a <= 0 and b <= 0:
        break
print(l)
