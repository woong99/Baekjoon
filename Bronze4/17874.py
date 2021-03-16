# Piece of Cake!

"""
2021/03/15 3:15 오후
정웅교
문제: https://www.acmicpc.net/problem/17874
"""
a, b, c = map(int, input().split())

if b < a / 2:
    n1 = a - b
else:
    n1 = b
if c < a / 2:
    n2 = a - c
else:
    n2 = c
print(n1 * n2 * 4)
