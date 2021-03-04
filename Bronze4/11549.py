# Identifying tea

"""
2021/03/04 2:30 오후
정웅교
문제: https://www.acmicpc.net/problem/11549
"""

n = int(input())
a, b, c, d, e = map(int, input().split())
ls = [a, b, c, d, e]
cnt = 0
for i in range(5):
    if ls[i] == n:
        cnt += 1
print(cnt)
