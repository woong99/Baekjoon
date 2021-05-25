# 행복

"""
2021/05/25 2:21 오후
정웅교
문제: https://www.acmicpc.net/problem/15969
"""

n = int(input())
ls = list(map(int, input().split()))
print(max(ls) - min(ls))
