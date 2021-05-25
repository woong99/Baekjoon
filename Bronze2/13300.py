# 방 배정

"""
2021/05/25 2:24 오후
정웅교
문제: https://www.acmicpc.net/problem/13300
"""
import math

n, k = map(int, input().split())
ls1 = [0, 0, 0, 0, 0, 0, ]
ls2 = [0, 0, 0, 0, 0, 0, ]
sum = 0
for _ in range(n):
    a, b = map(int, input().split())
    if a == 0:
        ls1[b - 1] += 1
    else:
        ls2[b - 1] += 1
for i in ls1:
    if i > k:
        sum += math.ceil(i / k)
    elif 0 < i <= k:
        sum += 1
for i in ls2:
    if i > k:
        sum += math.ceil(i / k)
    elif 0 < i <= k:
        sum += 1
print(sum)
