# 체스판 조각

"""
2021/03/01 4:42 오후
정웅교
문제: https://www.acmicpc.net/problem/3004
"""

n = int(input())

cnt = 2
k = 2
t = 2
while k <= n:
    cnt += t
    if k % 2 == 1:
        t += 1
    k += 1
print(cnt)
