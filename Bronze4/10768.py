# 특별한 날

"""
2021/02/28 5:35 오후
정웅교
문제: https://www.acmicpc.net/problem/10768
"""

a = int(input())
b = int(input())
if a < 2:
    print('Before')
elif a == 2:
    if b == 18:
        print('Special')
    elif b < 18:
        print('Before')
    else:
        print('After')
else:
    print('After')
