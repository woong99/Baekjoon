# 이상한 곱셈

"""
2021/05/27 12:13 오후
정웅교
문제: https://www.acmicpc.net/problem/1225
"""

a, b = map(str, input().split())
sum1 = 0
for i in b:
    sum1 += int(i)
sum = 0
for i in a:
    sum += int(i) * sum1
print(sum)
