# 피보나치

"""
2022/01/17 12:39 오후
정웅교
문제: https://www.acmicpc.net/problem/9711
"""
import sys

n = int(sys.stdin.readline())
for i in range(n):
    p, q = map(int, sys.stdin.readline().split())
    dp = [1, 1, 2]
    for j in range(3, p):
        dp.append((dp[j - 1] + dp[j - 2]) % q)
    print(f'Case #{i + 1}: {dp[p - 1]}')
