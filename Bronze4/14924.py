# 폰 노이만과 파리

"""
2021/03/01 5:20 오후
정웅교
문제: https://www.acmicpc.net/problem/14924
"""

a, b, c = map(int, input().split())
t = c // (a * 2)
print(b * t)
