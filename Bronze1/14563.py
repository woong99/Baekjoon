# 완전수

"""
2021/06/19 5:06 오전
정웅교
문제: https://www.acmicpc.net/problem/14563
"""


def sol(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum


n = int(input())
ls = list(map(int, input().split()))
for i in ls:
    if sol(i) == i:
        print('Perfect')
    elif sol(i) < i:
        print('Deficient')
    else:
        print('Abundant')
