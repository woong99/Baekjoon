# 루트

"""
2021/04/28 2:40 오후
정웅교
문제: https://www.acmicpc.net/problem/4619
"""

while 1:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    i = 1
    ls = []

    while i ** b < a:
        ls.append(abs(a - i ** b))
        i += 1
    ls.append(abs(a - i ** b))
    print(ls.index(min(ls)) + 1)
