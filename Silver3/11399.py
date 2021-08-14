# ATM

"""
2021/08/14 10:30 오전
정웅교
문제: https://www.acmicpc.net/problem/11399
"""

n = int(input())
ls = list(map(int, input().split()))
ls.sort()
sum1 = 0
for i in range(1, len(ls) + 1):
    sum1 += sum(ls[:i])
print(sum1)
