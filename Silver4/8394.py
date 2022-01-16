# 악수

"""
2022/01/16 10:49 오후
정웅교
문제: https://www.acmicpc.net/problem/8394
"""

n = int(input())
dp = [0, 2, 3]
for i in range(3, n):
    dp.append((dp[i - 1] + dp[i - 2]) % 10)
print(dp[n - 1])
