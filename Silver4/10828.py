# 스택

"""
 2021/07/01 8:37 오전
 정웅교
 문제: https://www.acmicpc.net/problem/10828
"""
from sys import stdin

ls = []
for _ in range(int(stdin.readline())):
    n = stdin.readline().split()
    if n[0] == 'size':
        print(len(ls))
    elif n[0] == 'empty':
        if len(ls) == 0:
            print(1)
        else:
            print(0)
    elif n[0] == 'top':
        if len(ls) == 0:
            print(-1)
        else:
            print(ls[len(ls) - 1])
    elif n[0] == 'pop':
        if len(ls) == 0:
            print(-1)
        else:
            print(ls[len(ls) - 1])
            del (ls[len(ls) - 1])
    elif n[0] == 'push':
        ls.append(int(n[1]))
