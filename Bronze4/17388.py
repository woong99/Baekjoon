# 와글와글 숭고한

"""
2021/03/01 5:11 오후
정웅교
문제: https://www.acmicpc.net/problem/17388
"""

a, b, c = map(int, input().split())
if a + b + c >= 100:
    print('OK')
else:
    if a < b < c or a < c < b:
        print('Soongsil')
    elif b < a < c or b < c < a:
        print('Korea')
    else:
        print('Hanyang')
