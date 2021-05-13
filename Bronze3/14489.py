# 치킨 두 마리 (...)

"""
2021/05/13 3:39 오후
정웅교
문제: https://www.acmicpc.net/problem/14489
"""

a, b = map(int, input().split())
c = int(input())
if a + b >= 2 * c:
    print(a + b - 2 * c)
else:
    print(a + b)
