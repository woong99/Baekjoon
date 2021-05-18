# 분수찾기

"""
2021/05/18 11:52 오후
정웅교
문제: https://www.acmicpc.net/problem/1193
"""

n = int(input())
a, b = 1, 1
stat = 0
cnt = 0
cnt1 = 0
for i in range(1, n):
    if cnt == cnt1 and stat == 0:
        cnt1 = 0
        b += 1
        cnt += 1
        stat = 1
    elif cnt1 != cnt and stat == 1:
        cnt1 += 1
        a += 1
        b -= 1
    elif cnt1 == cnt and stat == 1:
        cnt1 = 0
        a += 1
        cnt += 1
        stat = 0
    elif cnt1 != cnt and stat == 0:
        a -= 1
        b += 1
        cnt1 += 1
print(f"{a}/{b}")
