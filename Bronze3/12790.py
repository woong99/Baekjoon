# Mini Fantasy War

"""
2021/05/14 2:39 오후
정웅교
문제: https://www.acmicpc.net/problem/12790
"""

t = int(input())
for _ in range(t):
    a, b, c, d, a1, b1, c1, d1 = map(int, input().split())
    a2 = a + a1
    b2 = b + b1
    c2 = c + c1
    d2 = d + d1
    if a2 < 1:
        a2 = 1
    if b2 < 1:
        b2 = 1
    if c2 < 0:
        c2 = 0
    print(a2 + b2 * 5 + c2 * 2 + d2 * 2)
