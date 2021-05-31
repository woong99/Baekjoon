# 팰린드롬수

"""
2021/05/31 3:24 오후
정웅교
문제: https://www.acmicpc.net/problem/1259
"""
while 1:
    n = input()
    if n == '0':
        break
    s = n[::-1]
    if n == s:
        print('yes')
    else:
        print('no')
