# 오르막길

"""
2021/05/23 3:20 오후
정웅교
문제: https://www.acmicpc.net/problem/2846
"""
n = int(input())
ls = list(map(int, input().split()))
ls1 = []
sum = 0
for i in range(1, len(ls)):
    if ls[i - 1] < ls[i]:
        sum += ls[i] - ls[i - 1]
        ls1.append(sum)
    else:
        sum = 0
if len(ls1) == 0:
    print(0)
else:
    print(max(ls1))
