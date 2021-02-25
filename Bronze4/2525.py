# 오븐 시계

"""
2021/02/25 10:28 오후
정웅교
문제: https://www.acmicpc.net/problem/2525
"""

a, b = map(int, input().split())
n = int(input())
if b + n >= 60:
    a += (b + n) // 60
    b = b + n - 60
