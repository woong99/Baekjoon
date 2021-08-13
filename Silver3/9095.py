# 1, 2, 3 더하기

"""
2021/08/13 12:09 오후
정웅교
문제: https://www.acmicpc.net/problem/9095
"""

for _ in range(int(input())):
    n = int(input())
    dp = [1, 2, 4, 7]
    for i in range(4, n):
        dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])
    print(dp[n - 1])
