# 거스름돈

"""
2022/01/13 9:10 오후
정웅교
문제: https://www.acmicpc.net/problem/14916
"""
import sys

n = int(input())
dp = [sys.maxsize for _ in range(100001)]
dp[0] = sys.maxsize
dp[1] = sys.maxsize
dp[2] = 1
dp[3] = sys.maxsize
dp[4] = 2
dp[5] = 1
for i in range(6, n + 1):
    dp[i] = min(dp[i - 2], dp[i - 5]) + 1
if dp[n] == sys.maxsize:
    print(-1)
else:
    print(dp[n])
