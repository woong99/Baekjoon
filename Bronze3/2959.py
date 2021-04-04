# 거북이

"""
2021/04/04 3:15 오후
정웅교
문제: https://www.acmicpc.net/problem/2959
"""

a, b, c, d = map(int, input().split())
ls = [a, b, c, d]
ls.sort()
print(ls[0] * ls[2])
