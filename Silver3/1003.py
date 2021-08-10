# 피보나치 함수

"""
2021/08/10 10:35 오전
정웅교
문제: https://www.acmicpc.net/problem/1003
"""


def fib(n):
    length = len(zero)
    for i in range(length, n + 1):
        zero.append(zero[i - 1] + zero[i - 2])
        one.append(one[i - 1] + one[i - 2])


for _ in range(int(input())):
    n = int(input())
    zero = [1, 0, 1]
    one = [0, 1, 1]
    fib(n)
    print(zero[n], one[n])
