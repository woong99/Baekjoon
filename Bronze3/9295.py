# 주사위

"""
2021/05/03 2:24 오후
정웅교
문제: https://www.acmicpc.net/problem/9295
"""

n = int(input())
for i in range(1, n + 1):
    a, b = map(int, input().split())
    print(f"Case {i}: {a + b}")
