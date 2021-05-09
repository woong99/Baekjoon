# 별 찍기 - 15

"""
2021/05/09 5:38 오후
정웅교
문제: https://www.acmicpc.net/problem/10990
"""

n = int(input())
if n == 1:
    print('*')
else:
    print(' ' * (n - 1) + '*')
    for i in range(1, n):
        print(' ' * (n - i - 1) + '*' + ' ' * (2 * i - 1) + '*')
