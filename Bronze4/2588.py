# 곱셈

"""
2021/02/25 9:51 오후
정웅교
문제: https://www.acmicpc.net/problem/2588
"""

a = int(input())
b = int(input())

print(a * ((b % 100) % 10))
print(a * ((b % 100) // 10))
print(a * (b // 100))
print(a * b)
