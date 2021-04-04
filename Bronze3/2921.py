# 도미노

"""
2021/04/04 3:03 오후
정웅교
문제: https://www.acmicpc.net/problem/2921
"""

n = int(input())
sum = 3
a = 3
for i in range(1, n):
    a += 3 * (i + 1)
    sum += a
print(sum)
