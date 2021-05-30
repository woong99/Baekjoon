# 피보나치 수 2

"""
2021/05/30 10:35 오전
정웅교
문제: https://www.acmicpc.net/problem/2748
"""
n = int(input())
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    f = 0
    ff = 1
    sum = 1
    for i in range(2, n):
        f = ff
        ff = sum
        sum = f + ff
    print(sum)
