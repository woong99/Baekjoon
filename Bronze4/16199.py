# 나이 게산하기

"""
2021/03/05 12:03 오후
정웅교
문제: https://www.acmicpc.net/problem/16199
"""

a1, a2, a3 = map(int, input().split())
b1, b2, b3 = map(int, input().split())
if b1 > a1:
    b = b1 - a1 + 1
    c = b1 - a1
    if b2 >= a2 and b3 >= a3:
        a = b1 - a1
    else:
        a = b1 - a1 - 1
else:
    a = 0
    b = 1
    c = 0

print(a)
print(b)
print(c)
