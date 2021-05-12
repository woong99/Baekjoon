# 3n+1 수열

"""
2021/05/12 1:32 오후
정웅교
문제: https://www.acmicpc.net/problem/14920
"""

n = int(input())
cnt = 1
while 1:
    if n == 1:
        break
    if n % 2 == 0:
        n = n // 2
        cnt += 1
    elif n % 2 == 1:
        n = 3 * n + 1
        cnt += 1

print(cnt)
