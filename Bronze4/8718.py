# Bałwanek

"""
2021/03/20 2:45 오후
정웅교
문제: https://www.acmicpc.net/problem/8718
"""
x, k = map(int, input().split())
if k * 7 <= x:
    print(k * 7000)
elif k * 3.5 <= x:
    print(k * 3500)
elif k * 1.75 <= x:
    print(k * 1750)
else:
    print(0)
