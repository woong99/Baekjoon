# 더하기 4

"""
2021/05/10 4:25 오후
정웅교
문제: https://www.acmicpc.net/problem/11024
"""

n = int(input())
for _ in range(n):
    ls = list(map(int, input().split()))
    print(sum(ls))
