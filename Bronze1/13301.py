# 타일 장식물

"""
2022/01/14 2:57 오후
정웅교
문제: https://www.acmicpc.net/problem/13301
"""

n = int(input())
dp = [4, 6]
for i in range(2, n):
    dp.append(dp[i - 1] + dp[i - 2])
print(dp[n - 1])
