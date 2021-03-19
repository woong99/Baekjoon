# Volta

"""
2021/03/19 1:50 오후
정웅교
문제: https://www.acmicpc.net/problem/13610
"""
import math

a, b = map(int, input().split())
sum1 = 0
sum2 = 0
i = 0
while 1:
    sum1 += 1 / a
    sum2 += 1 / b
    i += 1
    if sum1 - sum2 >= 1:
        break
print(math.ceil(i * (1 / a)))
