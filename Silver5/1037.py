# 약수

"""
2021/06/28 10:56 오후
정웅교
문제: https://www.acmicpc.net/problem/1037
"""

n = int(input())
ls = list(map(int, input().split()))
ls.sort()
print(ls[0] * ls[len(ls) - 1])
