# 2의 제곱인가?

"""
2021/05/10 4:29 오후
정웅교
문제: https://www.acmicpc.net/problem/11966
"""
n = int(input())
if n == 1:
    print(1)
else:
    while n >= 1:
        n = n / 2
        if n == 1:
            print(1)
            break
if n != 1:
    print(0)
