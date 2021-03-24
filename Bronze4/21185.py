# Some Sum

"""
2021/03/24 5:23 오후
정웅교
문제: https://www.acmicpc.net/problem/21185
"""
n = int(input())
if n % 2 == 1:
    print('Either')
else:
    if n % 4 == 0:
        print('Even')
    else:
        print('Odd')
