# 지수연산

"""
2021/03/30 3:49 오후
정웅교
문제: https://www.acmicpc.net/problem/2052
"""

n = int(input())
s = '{:.300f}'.format(1 / 2 ** n)
k = len(s)
for i in range(k - 1, -1, -1):
    if s[i] != '0':
        k = i
        break
print(s[:k + 1])
print(s)
