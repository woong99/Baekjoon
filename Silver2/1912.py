# 연속합

"""
2021/08/29 4:18 오후
정웅교
문제: https://www.acmicpc.net/problem/1912
"""
n = int(input())
ls = list(map(int, input().split()))
dp = [0 for i in range(n)]
for i in range(n):
    dp[i] = max(ls[i], ls[i] + dp[i - 1])
print(max(dp))
