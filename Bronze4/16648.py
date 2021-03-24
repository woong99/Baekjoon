# Accumulator Battery

"""
2021/03/24 4:53 오후
정웅교
문제: https://www.acmicpc.net/problem/16648
"""
t, p = map(int, input().split())
if p >= 20:
    print((t / (100 - p) * (p + 20)))
else:
    print(t / (80 + (20 - p) * 2) * p * 2)
