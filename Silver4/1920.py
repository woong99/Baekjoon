# 수 찾기

"""
2021/07/01 11:34 오전
정웅교
문제: https://www.acmicpc.net/problem/1920
"""

from sys import stdin, stdout

n = int(stdin.readline())
ls1 = set(stdin.readline().split())
m = int(stdin.readline())
ls2 = stdin.readline().split()
for i in ls2:
    if i in ls1:
        stdout.write('1\n')
    else:
        stdout.write('0\n')
