# Petrol

"""
2021/03/24 4:43 오후
정웅교
문제: https://www.acmicpc.net/problem/18330
"""
n = int(input())
k = int(input())
if n <= 60:
    print(1500 * n)
else:
    if k + 60 > n:
        print(n * 1500)
    else:
        print((k + 60) * 1500 + (n - k - 60) * 3000)
