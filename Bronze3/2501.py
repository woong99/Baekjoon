# 약수 구하기

"""
2021/03/31 2:34 오후
정웅교
문제: https://www.acmicpc.net/problem/2501
"""

n, k = map(int, input().split())
i = 1
t = 0
while i <= n:
    if n % i == 0:
        t += 1
    if t == k:
        print(i)
        break
    i += 1
if i == n + 1:
    print(0)
