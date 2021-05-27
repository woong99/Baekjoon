# 숫자

"""
2021/05/27 12:40 오후
정웅교
문제: https://www.acmicpc.net/problem/10093
"""
a, b = map(int, input().split())
if a > b:
    a, b = b, a

if a == b:
    print(0)
else:
    print(b - a - 1)
    for i in range(a + 1, b):
        print(i, end=' ')
