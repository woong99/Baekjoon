# 윷놀이

"""
2021/03/31 2:30 오후
정웅교
문제: https://www.acmicpc.net/problem/2490
"""

for i in range(3):
    a, b, c, d = map(int, input().split())
    ls = [a, b, c, d]
    sum = 0
    for i in ls:
        if i == 1:
            sum += 1
    if sum == 0:
        print('D')
    elif sum == 1:
        print('C')
    elif sum == 2:
        print('B')
    elif sum == 3:
        print('A')
    else:
        print('E')
