# 별

"""
2021/06/24 8:58 오후
정웅교
문제: https://www.acmicpc.net/problem/16505
"""

import sys

N = int(input())
table = [[' '] * (1 << N) for _ in range(1 << N)]


def solve(x, y, n):
    if n == 1:
        table[x][y] = '*'
        return
    n //= 2
    solve(x, y, n)
    solve(x + n, y, n)
    solve(x, y + n, n)


solve(0, 0, 1 << N)
for i in table:
    sys.stdout.write(''.join(i).rstrip() + '\n')
