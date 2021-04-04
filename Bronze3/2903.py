# 중앙 이동 알고리즘

"""
2021/04/04 2:56 오후
정웅교
문제: https://www.acmicpc.net/problem/2903
"""

n = int(input())
b = 2
for i in range(n):
    b += 2 ** i
print(b ** 2)
