# 사분면

"""
2021/05/16 4:47 오후
정웅교
문제: https://www.acmicpc.net/problem/9610
"""

n = int(input())
q1, q2, q3, q4, axis = 0, 0, 0, 0, 0
for _ in range(n):
    a, b = map(int, input().split())
    if a > 0 and b > 0:
        q1 += 1
    elif a > 0 and b < 0:
        q4 += 1
    elif a < 0 and b > 0:
        q2 += 1
    elif a < 0 and b < 0:
        q3 += 1
    elif a == 0 and b == 0:
        axis += 1
    else:
        axis += 1
print(f"Q1: {q1}")
print(f"Q2: {q2}")
print(f"Q3: {q3}")
print(f"Q4: {q4}")
print(f"AXIS: {axis}")