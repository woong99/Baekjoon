# 파스칼 삼각형

"""
2022/01/11 4:44 오후
정웅교
문제: https://www.acmicpc.net/problem/15489
"""

r, c, w = map(int, input().split())
dp = [[0 for _ in range(w + c - 1)] for _ in range(r + w - 1)]
for i in range(r + w - 1):
    for j in range(w + c - 1):
        if j == 0 or j == i:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

sum = 0
cnt = -1
for i in range(r - 1, r + w - 1):
    cnt += 1
    for j in range(c - 1, c + cnt):
        sum += dp[i][j]
print(sum)
