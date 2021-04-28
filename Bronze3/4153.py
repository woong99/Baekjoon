# 직각삼각형

"""
2021/04/28 1:59 오후
정웅교
문제: https://www.acmicpc.net/problem/4153
"""

while 1:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    ls = [a, b, c]
    ls.sort()
    if ls[0] ** 2 + ls[1] ** 2 == ls[2] ** 2:
        print('right')
    else:
        print('wrong')
