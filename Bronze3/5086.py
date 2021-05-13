# 배수와 약수

"""
2021/05/13 4:04 오후
정웅교
문제: https://www.acmicpc.net/problem/5086
"""

while 1:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    if a % b == 0:
        print("multiple")
    elif b % a == 0:
        print("factor")
    else:
        print("neither")
