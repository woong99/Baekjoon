# 대회 or 인턴

"""
2021/04/03 2:27 오후
정웅교
문제: https://www.acmicpc.net/problem/2875
"""

n, m, k = map(int, input().split())
cnt = 0
while n + m >= k and n >= 0 and m >= 0:
    n -= 2
    m -= 1
    cnt += 1
print(cnt - 1)
