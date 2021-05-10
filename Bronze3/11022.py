# A+B-8

"""
2021/05/10 4:21 오후
정웅교
문제: https://www.acmicpc.net/problem/11022
"""

n = int(input())
for i in range(1, n + 1):
    a, b = map(int, input().split())
    print(f"Case #{i}: {a} + {b} = {a + b}")
