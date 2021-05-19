# 시험 감독

"""
2021/05/19 2:48 오후
정웅교
문제: https://www.acmicpc.net/problem/13458
"""

n = int(input())
ls = list(map(int, input().split()))
a, b = map(int, input().split())
cnt = 0
for i in ls:
    i -= a
    cnt += 1
    if i > 0:
        cnt += i // b
        if i % b > 0:
            cnt += 1
print(cnt)
