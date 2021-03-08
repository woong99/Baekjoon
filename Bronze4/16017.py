# Telemarketer or not?

"""
2021/03/08 3:12 오후
정웅교
문제: https://www.acmicpc.net/problem/16017
"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (a == 8 or a == 9) and (d == 8 or d == 9) and b == c:
    print('ignore')
else:
    print('answer')
