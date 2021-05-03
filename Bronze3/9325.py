# 얼마?

"""
2021/05/03 2:30 오후
정웅교
문제: https://www.acmicpc.net/problem/9325
"""

n = int(input())
for _ in range(n):
    p = int(input())
    i = int(input())
    result = p
    if i == 0:
        print(result)
    else:
        for _ in range(i):
            a, b = map(int, input().split())
            result += a * b
        print(result)
