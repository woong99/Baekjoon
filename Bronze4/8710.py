# Koszykarz

"""
2021/03/16 3:02 오후
정웅교
문제: https://www.acmicpc.net/problem/8710
"""

k, w, m = map(int, input().split())
n = w - k
if n % m == 0:
    print(n // m)
else:
    print(n // m + 1)
