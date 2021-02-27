# 시험 점수

"""
2021/02/27 10:46 오후
정웅교
문제: https://www.acmicpc.net/problem/5596
"""

a, b, c, d = map(int, input().split())
e, f, g, h = map(int, input().split())

n1 = a + b + c + d
n2 = e + f + g + h
if n1 < n2:
    print(n2)
elif n1 > n2:
    print(n1)
else:
    print(n1)
