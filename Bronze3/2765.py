# 자전거 속도

"""
2021/04/03 1:40 오후
정웅교
문제: https://www.acmicpc.net/problem/2765
"""
pi = 3.1415927
n = 1
while True:
    a, b, c = map(float, input().split())
    if b == 0:
        break
    dis = (a * pi * b) / (12 * 5280)
    mph = dis / (c / 3600)
    print(f'Trip #{n}: {round(dis, 2)} {format(round(mph, 2), ".2f")}')
    n += 1
