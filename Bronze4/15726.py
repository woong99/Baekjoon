# 이칙연산

"""
2021/03/03 10:46 오전
정웅교
문제: https://www.acmicpc.net/problem/15726
"""

a, b, c = map(int, input().split())
print(a * (max(b, c)) // (min(c, b)))
