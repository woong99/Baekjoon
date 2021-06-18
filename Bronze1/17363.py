# 우유가 넘어지면?

"""
2021/06/19 4:20 오전
정웅교
문제: https://www.acmicpc.net/problem/17363
"""
ls = []
a, b = map(int, input().split())
for _ in range(a):
    ls.append(list(input()))
for i in range(b):
    for k in range(a):
        s = ls[k][b - 1 - i]
        if s == '|':
            s = '-'
        elif s == '-':
            s = '|'
        elif s == '\\':
            s = '/'
        elif s == '>':
            s = '^'
        elif s == '/':
            s = '\\'
        elif s == '<':
            s = 'v'
        elif s == '^':
            s = '<'
        elif s == 'v':
            s = '>'
        print(s, end='')
    print()
