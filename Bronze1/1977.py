# 완전제곱수

"""
2021/05/30 10:45 오전
정웅교
문제: https://www.acmicpc.net/problem/1977
"""
import math

a = int(input())
b = int(input())
sum = 0

for i in range(math.ceil(math.sqrt(a)), math.trunc(math.sqrt(b)) + 1):
    sum += i * i
if sum == 0:
    print(-1)
else:
    print(sum)
    print((math.ceil(math.sqrt(a))) ** 2)
