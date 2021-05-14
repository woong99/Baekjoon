# 다면체

"""
2021/05/14 2:35 오후
정웅교
문제: https://www.acmicpc.net/problem/10569
"""
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(2 - a + b)
