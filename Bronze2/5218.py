# 알파벳 거리

"""
2021/05/26 1:49 오후
정웅교
문제: https://www.acmicpc.net/problem/5218
"""

for _ in range(int(input())):
    a, b = map(str, input().split())
    print('Distances:', end='')
    for i in range(len(a)):
        if ord(a[i]) <= ord(b[i]):
            print(f" {ord(b[i]) - ord(a[i])}", end='')
        else:
            print(f" {ord(b[i]) + 26 - ord(a[i])}", end='')
    print()
