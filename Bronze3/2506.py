# 점수계산

"""
2021/03/31 2:39 오후
정웅교
문제: https://www.acmicpc.net/problem/2506
"""

n = int(input())
ls = list(map(int, input().split()))
sum = 0
cnt = 0
for i in ls:
    if i == 1:
        sum += 1
        sum += cnt
        cnt += 1
    else:
        cnt = 0
print(sum)
