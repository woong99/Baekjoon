# X보다 작은 수

"""
2021/05/13 3:42 오후
정웅교
문제: https://www.acmicpc.net/problem/10871
"""
a, b = map(int, input().split())
ls = list(map(int, input().split()))
for i in ls:
    if i < b:
        print(i, end=' ')
