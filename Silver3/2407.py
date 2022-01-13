# 조합

"""
2022/01/13 9:20 오후
정웅교
문제: https://www.acmicpc.net/problem/2407
"""
n, m = map(int, input().split())
dp = [[0 for _ in range(101)] for _ in range(101)]
for i in range(n + 1):
    for j in range(m + 1):
        if j == 0 or i == j:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
print(dp[n][m])
