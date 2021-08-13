# 01타일

"""
2021/08/13 12:20 오후
정웅교
문제: https://www.acmicpc.net/problem/1904
"""

n = int(input())
dp = [1, 2, 3, 5]
for i in range(4, n + 1):
    dp.append((dp[i - 1] + dp[i - 2]) % 15746)
print(dp[n - 1])
