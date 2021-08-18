# Generations of Tribbles

"""
2021/08/18 1:37 오후
정웅교
문제: https://www.acmicpc.net/problem/9507
"""

n = int(input())
for _ in range(n):
    k = int(input())
    dp = [1, 1, 2, 4]
    for i in range(4, k + 1):
        dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 4])
    print(dp[k])
