# 문자열 반복

"""
2021/05/17 4:15 오후
정웅교
문제: https://www.acmicpc.net/problem/2675
"""

n = int(input())
for _ in range(n):
    a, b = map(str, input().split())
    for i in b:
        print(i * int(a), end='')
    print()
