# 3 つの整数

"""
2021/03/10 10:39 오후
정웅교
문제: https://www.acmicpc.net/problem/18408
"""
a, b, c = map(int, input().split())
ls = [a, b, c]
cnt1 = 0
cnt2 = 0
for i in range(len(ls)):
    if ls[i] == 1:
        cnt1 += 1
    else:
        cnt2 += 1
if cnt1 > cnt2:
    print('1')
else:
    print('2')
