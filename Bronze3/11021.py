# A+B-7

"""
2021/05/10 4:19 오후
정웅교
문제: https://www.acmicpc.net/problem/11021
"""

n = int(input())
for i in range(1, n + 1):
    a, b = map(int, input().split())
    print(f"Case #{i}: {a + b}")
