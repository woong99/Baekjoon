# 주사위 게임

"""
2021/05/04 2:10 오후
정웅교
문제: https://www.acmicpc.net/problem/10103
"""

n = int(input())
re1 = 100
re2 = 100
for _ in range(n):
    a, b = map(int, input().split())
    if a > b:
        re2 -= a
    elif a < b:
        re1 -= b
print(re1)
print(re2)
