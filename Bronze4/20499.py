# Darius님 한타 안 함?

"""
2021/03/08 2:52 오후
정웅교
문제: https://www.acmicpc.net/problem/20499
"""

n = input().split('/')
if int(n[0]) + int(n[2]) < int(n[1]) or int(n[1]) == 0:
    print('hasu')
else:
    print('gosu')
