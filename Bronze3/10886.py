# 0 = not cute / 1 = cute

"""
2021/05/09 5:22 오후
정웅교
문제: https://www.acmicpc.net/problem/10886
"""
n = int(input())
cnt1 = 0
cnt2 = 0
for _ in range(n):
    a = int(input())
    if a == 1:
        cnt1 += 1
    else:
        cnt2 += 1
if cnt1 > cnt2:
    print('Junhee is cute!')
elif cnt2 > cnt1:
    print('Junhee is not cute!')
