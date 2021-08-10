# 2*n 타일링

"""
2021/08/10 11:20 오전
정웅교
문제: https://www.acmicpc.net/problem/11726
"""


def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 3
    elif ls[n] != 0:
        return ls[n]
    else:
        ls[n] = fib(n - 1) + fib(n - 2)
        return ls[n]


n = int(input())
ls = [0 for i in range(n + 1)]
print(fib(n) % 10007)
