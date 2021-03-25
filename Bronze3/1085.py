# 직사각형에서 탈출

"""
2021/03/25 3:54 오후
정웅교
문제: https://www.acmicpc.net/problem/1085
"""

x, y, w, h = map(int, input().split())
print(min(w - x, x, y, h - y))
