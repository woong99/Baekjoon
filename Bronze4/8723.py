# Patyki

"""
2021/03/19 1:43 오후
정웅교
문제: https://www.acmicpc.net/problem/8723
"""
a, b, c = map(int, input().split())
ls = [a, b, c]
ls.sort()
if a == b and b == c:
    print('2')
elif ls[0] ** 2 + ls[1] ** 2 == ls[2] ** 2:
    print('1')
else:
    print('0')
