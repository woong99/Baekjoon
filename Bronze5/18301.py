# Rats

"""
2021/02/25 6:00 오후
정웅교
문제: https://www.acmicpc.net/problem/18301
"""

a, b, c = map(int, input().split())
print((a + 1) * (b + 1) // (c + 1) - 1)
