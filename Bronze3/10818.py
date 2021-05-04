# 최소, 최대

"""
2021/05/04 2:48 오후
정웅교
문제: https://www.acmicpc.net/problem/10818
"""

n = int(input())
ls = list(map(int, input().split()))
ls.sort()
print(ls[0], ls[len(ls) - 1])
