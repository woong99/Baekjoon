# 플러그

"""
2021/03/30 3:38 오후
정웅교
문제: https://www.acmicpc.net/problem/2010
"""
n = int(input())
sum = 0
for i in range(n):
    k = int(input())
    sum += k - 1
sum += 1
print(sum)
