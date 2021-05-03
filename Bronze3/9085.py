# 더하기

"""
2021/05/03 2:17 오후
정웅교
문제: https://www.acmicpc.net/problem/9085
"""
n = int(input())
for _ in range(n):
    i = int(input())
    ls = list(map(int, input().split()))
    result = 0
    for k in ls:
        result += k
    print(result)
