# Baseball

"""
2021/05/14 2:32 오후
정웅교
문제: https://www.acmicpc.net/problem/10214
"""

n = int(input())
for _ in range(n):
    sum1, sum2 = 0, 0
    for _ in range(9):
        a, b = map(int, input().split())
        sum1 += a
        sum2 += b
    if sum1 > sum2:
        print('Yonsei')
    elif sum2 > sum1:
        print('Korea')
    else:
        print('Draw')
