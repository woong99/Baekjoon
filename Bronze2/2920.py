# 음계

"""
2021/05/18 10:35 오후
정웅교
문제: https://www.acmicpc.net/problem/2920
"""

n = list(map(int, input().split()))
a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [8, 7, 6, 5, 4, 3, 2, 1]
cnt1, cnt2 = 0, 0
for i in range(len(n)):
    if n[i] == a[i]:
        cnt1 += 1
for i in range(len(n)):
    if n[i] == b[i]:
        cnt2 += 1
if cnt1 == 8:
    print('ascending')
elif cnt2 == 8:
    print('descending')
else:
    print('mixed')
