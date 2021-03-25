# 부호

"""
2021/03/25 3:57 오후
정웅교
문제: https://www.acmicpc.net/problem/1247
"""
for _ in range(3):
    n = int(input())
    sum = 0
    for _ in range(n):
        n = int(input())
        sum += n
    if sum == 0:
        print(0)
    elif sum > 0:
        print('+')
    else:
        print('-')
