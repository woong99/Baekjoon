# 주사위 세개

"""
2021/02/26 10:31 오후
정웅교
문제: https://www.acmicpc.net/problem/2480
"""

a, b, c = map(int, input().split())
if a == b == c:
    print(10000 + (a * 1000))
elif a == b:
    print(1000 + (a * 100))
elif a == c:
    print(1000 + (a * 100))
elif b == c:
    print(1000 + (b * 100))
else:
    ls = [a, b, c]
    ls.sort()
    print(ls[2] * 100)
