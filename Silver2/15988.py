# 1, 2, 3 더하기 3

"""
2021/08/19 12:21 오후
정웅교
문제: https://www.acmicpc.net/problem/15988
"""
from sys import stdin

dp = [1, 2, 4]
for i in range(3, 1000000):
    dp.append((dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000009)
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    print(dp[n - 1])
