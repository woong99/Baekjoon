# 피자 (Small)

"""
2022/01/17 12:15 오후
정웅교
문제: https://www.acmicpc.net/problem/14606
"""

n = int(input())
dp = [0, 0]
for i in range(2, n + 1):
    dp.append(dp[i - 1] + i - 1)
print(dp[n])
