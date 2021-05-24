# ABC

"""
2021/05/24 3:36 오후
정웅교
문제: https://www.acmicpc.net/problem/3047
"""

a = list(map(int, input().split()))
a.sort()
s = input()
dic = {'A': a[0], 'B': a[1], 'C': a[2]}
for i in s:
    print(dic[i], end=' ')
print()
