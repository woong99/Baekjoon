# Covid-19

"""
2021/03/23 10:10 오후
정웅교
문제: https://www.acmicpc.net/problem/20673
"""
p = int(input())
q = int(input())
if p <= 50 and q <= 10:
    print('White')
elif q >= 30:
    print('Red')
else:
    print('Yellow')
