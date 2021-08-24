# 가장 큰 증가 부분 수열

"""
2021/08/23 10:27 오후
정웅교
문제: https://www.acmicpc.net/problem/11055
"""
n = int(input())
ls = list(map(int, input().split()))
dp = ls[:]
for i in range(n):
    for j in range(i):
        if ls[j] < ls[i]:
            dp[i] = max(dp[i], ls[i] + dp[j])
print(max(dp))
