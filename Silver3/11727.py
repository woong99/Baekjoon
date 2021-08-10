# 2×n 타일링 2

"""
2021/08/10 11:37 오전
정웅교
문제: https://www.acmicpc.net/problem/11727
"""

n = int(input())
ls = [1, 3, 5]
for i in range(3, n + 1):
    ls.append(ls[i - 1] + 2 * ls[i - 2])
print(ls[n - 1] % 10007)
