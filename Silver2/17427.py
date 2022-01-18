# 약수의 합 2

"""
2022/01/18 1:07 오후
정웅교
문제: https://www.acmicpc.net/problem/17427
"""

n = int(input())
v = 1
sum = 0
for i in range(1, n + 1):
    sum += (n // i) * i
print(sum)
