# 세수정렬

"""
2021/02/26 10:17 오후
정웅교
문제: https://www.acmicpc.net/problem/2752
"""

a, b, c = map(int, input().split())
if a < b < c:
    print(a, b, c)
elif a < c < b:
    print(a, c, b)
elif b < a < c:
    print(b, a, c)
elif b < c < a:
    print(b, c, a)
elif c < a < b:
    print(c, a, b)
else:
    print(c, b, a)
