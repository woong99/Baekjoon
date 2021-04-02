# 삼각수의 합

"""
2021/04/02 6:47 오후
정웅교
문제: https://www.acmicpc.net/problem/2721
"""


def tri(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum


n = int(input())
for i in range(n):
    k = int(input())
    sum = 0
    for j in range(1, k + 1):
        sum += j * tri(j + 1)
    print(sum)
