# 1로 만들기

"""
2021/08/13 11:16 오전
정웅교
문제: https://www.acmicpc.net/problem/1463
"""

n = int(input())
dp = [0, 0, 1, 1]
for i in range(4, n + 1):
    dp.append(dp[i - 1] + 1)

    if i % 2 == 0:
        dp[i] = min(dp[i // 2] + 1, dp[i])

    if i % 3 == 0:
        dp[i] = min(dp[i // 3] + 1, dp[i])
print(dp[n])
