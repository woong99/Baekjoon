# BABBA

"""
2021/06/05 1:11 오전
정웅교
문제: https://www.acmicpc.net/problem/9625
"""
n = int(input())
a, b = 0, 1
if n == 1:
    print(a, b)
else:
    for i in range(1, n):
        temp = a
        a = b
        b = a + temp
    print(a, b)
