# Square Pasture

"""
2021/03/06 10:30 오전
정웅교
문제: https://www.acmicpc.net/problem/14173
"""
a, b, c, d = map(int, input().split())
e, f, g, h = map(int, input().split())
ls1 = [a, c, e, g]
ls2 = [b, d, f, h]
n1 = max(ls1) - min(ls1)
n2 = max(ls2) - min(ls2)
if n1 >= n2:
    print(n1 ** 2)
else:
    print(n2 ** 2)
