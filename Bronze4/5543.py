# 상근날드

"""
2021/02/25 10:18 오후
정웅교
문제: https://www.acmicpc.net/problem/5543
"""

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

ls1 = [a, b, c]
ls1.sort()
ls2 = [d, e]
ls2.sort()
print(ls1[0] + ls2[0] - 50)
