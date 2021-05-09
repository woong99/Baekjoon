# 별 찍기 - 17

"""
2021/05/09 6:12 오후
정웅교
문제: https://www.acmicpc.net/problem/10992
"""

n = int(input())
if n == 1:
    print('*')
else:
    print(" " * (n - 1) + '*')
    for i in range(n - 2):
        print(' ' * (n - i - 2) + '*' + ' ' * (2 * i + 1) + '*')
    print('*' * (2 * n - 1))
