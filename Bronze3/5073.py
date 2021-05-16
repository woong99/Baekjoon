# 삼각형과 세 변

"""
2021/05/17 12:42 오전
정웅교
문제: https://www.acmicpc.net/problem/5073
"""

while 1:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    ls = [a, b, c]
    ls.sort()
    if ls[0] + ls[1] <= ls[2]:
        print('Invalid')
    else:
        if a == b == c:
            print('Equilateral')
        elif a != b and b != c and c != a:
            print('Scalene')
        else:
            print('Isosceles')
