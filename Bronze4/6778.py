# Which Alien?

"""
2021/03/15 3:06 오후
정웅교
문제: https://www.acmicpc.net/problem/6778
"""
a = int(input())
b = int(input())
if a >= 3 and b <= 4:
    print('TroyMartian')
if a <= 6 and b >= 2:
    print('VladSaturnian')
if a <= 2 and b <= 3:
    print('GraemeMercurian')
