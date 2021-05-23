# 별 찍기 - 20

"""
2021/05/23 2:45 오후
정웅교
문제: https://www.acmicpc.net/problem/10995
"""
n = int(input())
if n == 1:
    print('*')
else:
    for i in range(n):
        if i % 2 == 0:
            print('* ' * n)
        else:
            print(' ' + '* ' * n)
