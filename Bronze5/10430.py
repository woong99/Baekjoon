# 나머

"""
2021/02/22 9:11 오후
정웅교
문제: https://www.acmicpc.net/problem/10430
"""
a, b, c = map(int, input().split())
print((a + b) % c)
print(((a % c) + (b % c)) % c)
print((a * b) % c)
print((a % c) * (b % c) % c)
