# 삼각형 외우기

"""
2021/02/27 10:37 오후
정웅교
문제: https://www.acmicpc.net/problem/10101
"""

a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print('Equilateral')
elif a + b + c != 180:
    print('Error')
elif a + b + c == 180:
    if a != b and b != c and c != a:
        print('Scalene')
    else:
        print('Isosceles')
