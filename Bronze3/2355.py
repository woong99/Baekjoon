# 시그마

"""
2021/03/30 4:26 오후
정웅교
문제: https://www.acmicpc.net/problem/2355
"""
a, b = map(int, input().split())
if a > b:
    temp = a
    a = b
    b = temp
k1 = a + b
k2 = b - a
print(int(k1 * (k2 + 1) / 2))
