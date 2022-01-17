# 피자 (Large)

"""
2022/01/17 12:28 오후
정웅교
문제: https://www.acmicpc.net/problem/14607
"""
import sys

n = int(sys.stdin.readline())
dp = [0, 1]
for i in range(2, n):
    if i % 2 == 0:
        dp[0] = dp[1] + i
    else:
        dp[1] = dp[0] + i
    # dp.append(dp[i - 1] + i)
if n % 2 == 0:
    print(dp[1])
else:
    print(dp[0])
