# 별 찍기 - 16

"""
2021/05/09 6:03 오후
정웅교
문제: https://www.acmicpc.net/problem/10991
"""

n = int(input())
if n == 1:
    print('*')
else:
    print(' ' * (n - 1) + '*')
    for i in range(1, n):
        print(' ' * (n - 1 - i) + '*', end='')
        for k in range(i):
            print(' *', end='')
        print()
