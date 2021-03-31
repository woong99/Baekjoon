# 주사위 게임

"""
2021/03/31 2:21 오후
정웅교
문제: https://www.acmicpc.net/problem/2476
"""
n = int(input())
ls = []
for i in range(n):
    sum = 0
    a, b, c = map(int, input().split())
    if a == b and b == c:
        sum = 10000 + a * 1000
    elif a == b and b != c:
        sum = 1000 + a * 100
    elif b == c and c != a:
        sum = 1000 + b * 100
    elif c == a and a != b:
        sum = 1000 + c * 100
    else:
        sum = max(a, b, c) * 100
    ls.append(sum)
ls.sort()
print(ls[n - 1])
