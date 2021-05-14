# 상금 헌터

"""
2021/05/14 2:19 오후
정웅교
문제: https://www.acmicpc.net/problem/15953
"""

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    sum = 0
    if a == 1:
        sum += 5000000
    elif 2 <= a <= 3:
        sum += 3000000
    elif 4 <= a <= 6:
        sum += 2000000
    elif 7 <= a <= 10:
        sum += 500000
    elif 11 <= a <= 15:
        sum += 300000
    elif 16 <= a <= 21:
        sum += 100000
    if b == 1:
        sum += 5120000
    elif 2 <= b <= 3:
        sum += 2560000
    elif 4 <= b <= 7:
        sum += 1280000
    elif 8 <= b <= 15:
        sum += 640000
    elif 16 <= b <= 31:
        sum += 320000
    print(sum)
