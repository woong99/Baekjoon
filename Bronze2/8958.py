# OX퀴즈

"""
2021/05/17 2:06 오전
정웅교
문제: https://www.acmicpc.net/problem/8958
"""

n = int(input())
for _ in range(n):
    a = list(str(input()))
    sum = 0
    stat = 1
    cnt = 0
    for i in range(len(a)):
        if a[i] == 'O' and stat == 1:
            sum += 1
            sum += cnt
            cnt += 1
        elif a[i] == 'O' and stat == 0:
            sum += 1
            stat = 1
            cnt += 1
        elif a[i] == 'X':
            stat = 0
            cnt = 0
    print(sum)
