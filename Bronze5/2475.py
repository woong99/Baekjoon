# 검증수

"""
2021/02/22 9:34 오후
정웅교
문제: https://www.acmicpc.net/problem/2475
"""
a, b, c, d, e = map(int, input().split())
sum = a ** 2 + b ** 2 + c ** 2 + d ** 2 + e ** 2
print(sum % 10)
