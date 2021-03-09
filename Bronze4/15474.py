# 鉛筆

"""
2021/03/09 5:40 오후
정웅교
문제: https://www.acmicpc.net/problem/15474
"""
n, a, b, c, d = map(int, input().split())
if n % a == 0:
    n1 = n // a
else:
    n1 = n // a + 1
if n % c == 0:
    n2 = n // c
else:
    n2 = n // c + 1
if n1 * b < n2 * d:
    print(n1 * b)
else:
    print(n2 * d)
