# 덱

"""
2021/07/01 8:15 오후
정웅교
문제: https://www.acmicpc.net/problem/10866
"""
from sys import stdin

ls = []
for _ in range(int(stdin.readline())):
    cmd = stdin.readline().split()
    if cmd[0] == 'push_front':
        ls.insert(0, cmd[1])
    elif cmd[0] == 'push_back':
        ls.append(cmd[1])
    elif cmd[0] == 'pop_front':
        if len(ls) == 0:
            print(-1)
        else:
            print(ls[0])
            del (ls[0])
    elif cmd[0] == 'pop_back':
        if len(ls) == 0:
            print(-1)
        else:
            print(ls.pop())
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
