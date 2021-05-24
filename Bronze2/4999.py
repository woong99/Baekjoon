# 아!

"""
2021/05/24 3:32 오후
정웅교
문제: https://www.acmicpc.net/problem/4999
"""

a = input()
b = input()
if a.count('a') >= b.count('a'):
    print('go')
elif a == 'h' and b == 'h':
    print('go')
else:
    print('no')
