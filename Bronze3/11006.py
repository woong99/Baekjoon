# 남욱이의 닭장

"""
2021/05/09 7:12 오후
정웅교
문제: https://www.acmicpc.net/problem/11006
"""

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(b * 2 - a, b - (b * 2 - a))
