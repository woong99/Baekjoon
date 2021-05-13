# TGN

"""
2021/05/13 4:08 오후
정웅교
문제: https://www.acmicpc.net/problem/5063
"""

n = int(input())
for _ in range(n):
    a, b, c = map(int, input().split())
    if b - c > a:
        print('advertise')
    elif b - c == a:
        print('does not matter')
    else:
        print('do not advertise')
