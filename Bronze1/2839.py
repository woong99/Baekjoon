# 설탕 배달

"""
2022/01/14 2:44 오후
정웅교
문제: https://www.acmicpc.net/problem/2839
"""
import sys

n = int(sys.stdin.readline())
dp = [sys.maxsize for _ in range(5001)]
dp[3] = 1
dp[5] = 1
for i in range(6, n + 1):
    if dp[i - 3] == sys.maxsize and dp[i - 5] == sys.maxsize:
        dp[i] = sys.maxsize
    else:
        dp[i] = min(dp[i - 3], dp[i - 5]) + 1
if dp[n] == sys.maxsize:
    print(-1)
else:
    print(dp[n])
