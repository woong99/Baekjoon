# Dominos

"""
2021/03/11 1:47 오후
정웅교
문제: https://www.acmicpc.net/problem/15236
"""
n = int(input())
sum = 0
stack = 0
for i in range(n):
    stack += 3 * (i + 1)
    sum += stack
print(sum)
