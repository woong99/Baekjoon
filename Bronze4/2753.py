# 윤년

"""
2021/02/25 9:48 오후
정웅교
문제: https://www.acmicpc.net/problem/2753
"""

n = int(input())
if n % 4 == 0:
    if n % 400 == 0:
        print('1')
    elif n % 100 != 0:
        print('1')
    else:
        print('0')
else:
    print('0')
