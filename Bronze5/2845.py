# 파티가 끝나고 난 뒤

"""
2021/02/22 10:46 오후
정웅교
문제: https://www.acmicpc.net/problem/2845
"""

a, b = map(int, input().split())
c, d, e, f, g = map(int, input().split())
n = a * b
print((c - n), (d - n), (e - n), (f - n), (g - n))
