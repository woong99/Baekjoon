# 사분면 고르기

"""
2021/02/25 9:55 오후
정웅교
문제: https://www.acmicpc.net/problem/14681
"""

a = int(input())
b = int(input())

if a > 0 and b > 0:
    print('1')
elif a > 0 and b < 0:
    print('4')
elif a < 0 and b > 0:
    print('2')
else:
    print('3')
