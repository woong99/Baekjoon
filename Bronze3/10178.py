# 할로윈의 사탕

"""
2021/05/03 2:53 오후
정웅교
문제: https://www.acmicpc.net/problem/10178
"""

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(f"You get {a // b} piece(s) and your dad gets {a - (a // b) * b} piece(s).")
