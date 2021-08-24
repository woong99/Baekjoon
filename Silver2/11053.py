# 가장 긴 증가하는 부분 수열

"""
2021/08/23 10:13 오후
정웅교
문제: https://www.acmicpc.net/problem/11053
"""

n = int(input())
ls = list(map(int, input().split()))
dp = [1] * n
for i in range(n):
    for j in range(i):
        if ls[j] < ls[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
