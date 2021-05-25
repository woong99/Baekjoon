# 카드게임

"""
2021/05/25 2:49 오후
정웅교
문제: https://www.acmicpc.net/problem/10801
"""

a = list(map(int, input().split()))
b = list(map(int, input().split()))
sum1 = 0
sum2 = 0
for i in range(10):
    if a[i] > b[i]:
        sum1 += 1
    elif a[i] < b[i]:
        sum2 += 1
if sum1 > sum2:
    print('A')
elif sum1 < sum2:
    print('B')
else:
    print('D')
