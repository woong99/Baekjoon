# Judging Moose

"""
2021/03/14 3:59 오후
정웅교
문제: https://www.acmicpc.net/problem/15025
"""
a, b = map(int, input().split())
if a == 0 and b == 0:
    print('Not a moose')
elif a != b:
    if a > b:
        print('Odd', a * 2)
    else:
        print('Odd', b * 2)
else:
    print('Even', a * 2)
