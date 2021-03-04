# 카드 뽑기

"""
2021/03/04 2:39 오후
정웅교
문제: https://www.acmicpc.net/problem/16204
"""

n, m, k = map(int, input().split())
cnt = 0
if m >= k:
    cnt += k
else:
    cnt += m
if n - m >= n - k:
    cnt += n - k
else:
    cnt += n - m

print(cnt)
