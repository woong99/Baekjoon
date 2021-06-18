# 피시방 알바

"""
2021/06/17 5:26 오후
정웅교
문제: https://www.acmicpc.net/problem/1453
"""

n = int(input())
ls = list(map(int, input().split()))
ls1 = []
cnt1 = 0
for i in ls:
    if i in ls1:
        cnt1 += 1
    else:
        ls1.append(i)
print(cnt1)
