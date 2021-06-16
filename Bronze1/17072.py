# 아스키 아

"""
2021/06/16 3:37 오후
정웅교
문제: https://www.acmicpc.net/problem/17072
"""


def convert(a, b, c):
    sum = 2126 * a + 7152 * b + 722 * c
    if 0 <= sum < 510000:
        return '#'
    elif 510000 <= sum < 1020000:
        return 'o'
    elif 1020000 <= sum < 1530000:
        return '+'
    elif 1530000 <= sum < 2040000:
        return '-'
    else:
        return '.'


a, b = map(int, input().split())
for _ in range(a):
    ls = list(map(int, input().split()))
    for i in range(b):
        print(convert(ls[3 * i], ls[3 * i + 1], ls[3 * i + 2]), end='')
    print()
