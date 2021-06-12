# 이진수 덧셈

"""
2021/06/11 2:49 오후
정웅교
문제: https://www.acmicpc.net/problem/1252
"""

a, b = map(str, input().split())
d = int(a, 2) + int(b, 2)
print(bin(d)[2:])
