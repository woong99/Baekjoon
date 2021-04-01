# 사탕 선생 고창영

"""
2021/04/01 1:29 오후
정웅교
문제: https://www.acmicpc.net/problem/2547
"""
t = int(input())
blank = input()
for i in range(t):
    n = int(input())
    sum = 0
    for _ in range(n):
        k = int(input())
        sum += k
    if sum % n == 0:
        print('YES')
    else:
        print('NO')
    if i != t - 1:
        blank = input()
