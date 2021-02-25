# 10부제

"""
2021/02/25 10:24 오후
정웅교
문제: https://www.acmicpc.net/problem/10797
"""

n = int(input())
a, b, c, d, e = map(int, input().split())
cnt = 0
ls = [a, b, c, d, e]
for i in range(5):
    if ls[i] == n:
        cnt += 1
print(cnt)
