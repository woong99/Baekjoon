# 과자

"""
2021/02/27 10:05 오전
정웅교
문제: https://www.acmicpc.net/problem/10156
"""

a, b, c = map(int, input().split())
n = a * b - c
if n <= 0:
    print('0')
else:
    print(n)
