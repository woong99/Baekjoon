# 가장 긴 감소하는 부분 수열

"""
2021/08/24 7:36 오후
정웅교
문제: https://www.acmicpc.net/problem/11722
"""

n = int(input())
ls = list(map(int, input().split()))
dp = [1] * n
for i in range(n):
    for j in range(i):
        if ls[i] < ls[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
