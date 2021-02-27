# 수도요금

"""
2021/02/27 10:41 오후
정웅교
문제: https://www.acmicpc.net/problem/10707
"""

a = int(input())
b = int(input())
c = int(input())
d = int(input())
p = int(input())

n1 = a * p
if p <= c:
    n2 = b
else:
    n2 = b + (p - c) * d
    
if n1 < n2:
    print(n1)
else:
    print(n2)
