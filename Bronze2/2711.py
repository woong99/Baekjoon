# 오타맨 고창영

"""
2021/05/26 12:58 오후
정웅교
문제: https://www.acmicpc.net/problem/2711
"""

for _ in range(int(input())):
    a, b = map(str, input().split())
    print(b[:int(a) - 1] + b[int(a):])
