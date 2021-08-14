# 제곱수의 합

"""
2021/08/14 10:39 오전
정웅교
문제: https://www.acmicpc.net/problem/1699
"""
n = int(input())
dp = [0 for i in range(n + 1)]
square = [i * i for i in range(1, 317)]
for i in range(1, n + 1):
    s = []
    for j in square:
        if j > i:
            break
        s.append(dp[i - j])
    dp[i] = min(s) + 1
print(dp[n])
