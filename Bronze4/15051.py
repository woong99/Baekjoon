# Máquina de café

"""
2021/03/20 3:05 오후
정웅교
문제: https://www.acmicpc.net/problem/15051
"""
A1 = int(input())
A2 = int(input())
A3 = int(input())
r1 = A2 * 2 + A3 * 4
r2 = A1 * 2 + A3 * 2
r3 = A1 * 4 + A2 * 2
print(min(r1, r2, r3))
