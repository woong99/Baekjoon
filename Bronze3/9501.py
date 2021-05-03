# 꿍의 우주여행

"""
2021/05/03 2:43 오후
정웅교
문제: https://www.acmicpc.net/problem/9501
"""
t = int(input())
for _ in range(t):
    n, d = map(int, input().split())
    cnt = 0
    for _ in range(n):
        v, f, c = map(int, input().split())
        if v * (f / c) >= d:
            cnt += 1
    print(cnt)
