# 파스칼의 삼각형

"""
2022/01/11 4:34 오후
정웅교
문제: https://www.acmicpc.net/problem/16395
"""
n, k = map(int, input().split())
dp = [[0 for _ in range(k)] for _ in range(n)]
for i in range(n):
    for j in range(k):
        if j == 0 or j == i:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
print(dp[n - 1][k - 1])
