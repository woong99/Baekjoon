# 다음수

"""
2021/04/29 2:04 오후
정웅교
문제: https://www.acmicpc.net/problem/4880
"""

while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    a1 = b - a
    a2 = c - b
    if a != 0 and b != 0:
        a3 = b / a
    if a1 == a2:
        print(f"AP {c + a1}")
    if a3 * b == c:
        print(f"GP {int(c * a3)}")
