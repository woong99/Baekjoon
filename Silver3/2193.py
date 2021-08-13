# 이친수

"""
2021/08/13 10:19 오전
정웅교
문제: https://www.acmicpc.net/problem/2193
"""

n = int(input())
ls = [1, 1, 2]
for i in range(3, n):
    ls.append(ls[i - 1] + ls[i - 2])
print(ls[n - 1])
