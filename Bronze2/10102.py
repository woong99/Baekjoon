# 개표

"""
2021/05/27 12:28 오후
정웅교
문제: https://www.acmicpc.net/problem/10102
"""
n = int(input())
s = input()
sum1 = 0
sum2 = 0
for i in s:
    if i == 'A':
        sum1 += 1
    else:
        sum2 += 1
if sum1 > sum2:
    print('A')
elif sum1 < sum2:
    print('B')
else:
    print('Tie')
