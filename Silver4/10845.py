# 큐

"""
2021/07/01 8:50 오전
정웅교
문제: https://www.acmicpc.net/problem/10845
"""
from sys import stdin

ls = []
for _ in range(int(stdin.readline())):
    cmd = stdin.readline().split()
    if cmd[0] == 'push':
        ls.append(cmd[1])
    elif cmd[0] == 'pop':
        if len(ls) == 0:
            print(-1)
        else:
            print(ls[0])
            del (ls[0])
    elif cmd[0] == 'size':
        print(len(ls))
    elif cmd[0] == 'empty':
        if len(ls) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if len(ls) == 0:
            print(-1)
        else:
            print(ls[0])
    elif cmd[0] == 'back':
        if len(ls) == 0:
            print(-1)
        else:
            print(ls[len(ls) - 1])
