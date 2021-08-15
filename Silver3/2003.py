# 수들의 합 2

"""
2021/08/15 9:55 오전
정웅교
문제: https://www.acmicpc.net/problem/2003
"""
n, m = map(int, input().split())
ls = list(map(int, input().split()))
cnt = 0

left, right = 0, 1
while left <= len(ls) - 1:
    sum1 = sum(ls[left:right])
    if sum1 == m:
        cnt += 1
        left += 1
        right = left + 1
    elif sum1 > m:
        left += 1
        right = left + 1
    else:
        right += 1
        if right >= len(ls) + 1:
            left += 1
print(cnt)
