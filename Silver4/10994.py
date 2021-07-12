# 별 찍기 - 19

"""
2021/07/12 2:40 오후
정웅교
문제: https://www.acmicpc.net/problem/10994
"""

n = int(input())
if n == 1:
    print('*')
else:
    print('*' * (4 * n - 3))
    for i in range(2 * n - 3):
        if i % 2 == 0:
            print('* ' * (i // 2 + 1) + ' ' * ((4 * n - 7) - 4 * (i // 2)) + ' *' * (i // 2 + 1))
        else:
            print('* ' * (i // 2 + 1) + '*' * ((4 * n - 7) - 4 * (i // 2)) + ' *' * (i // 2 + 1))
    print('* ' * (2 * n - 2) + '*')
    for i in range(2 * n - 3):
        if i % 2 == 0:
            print('* ' * (-(i // 2 + 1) + n) + ' ' * (2 * i + 1) + ' *' * (-(i // 2 + 1) + n))
        else:
            print('* ' * (-(i // 2) + n - 2) + '*' * (2 * i + 3) + ' *' * (-(i // 2 + 1) + n - 1))
    print('*' * (4 * n - 3))
