# 2차원 배열의 합

"""
2021/06/17 4:44 오후
정웅교
문제: https://www.acmicpc.net/problem/2167
"""

n, m = map(int, input().split())
ls = []
for _ in range(n):
    a = list(map(int, input().split()))
    ls.append(a)
for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    sum = 0
    if a == c and b != d:
        for i in range(b, d + 1):
            sum += ls[a - 1][i - 1]
    elif a == c and b == d:
        sum = ls[a - 1][b - 1]
    elif b == d and a != c:
        for i in range(a, c + 1):
            sum += ls[i - 1][b - 1]
    else:
        for i in range(a, c + 1):
            for k in range(b, d + 1):
                sum += ls[i - 1][k - 1]
    print(sum)
