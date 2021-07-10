# 차집합

"""
2021/07/02 5:22 오후
정웅교
문제: https://www.acmicpc.net/problem/1822
"""
a, b = map(int, input().split())
s1 = set(list(map(int, input().split())))
s2 = set(list(map(int, input().split())))
s4 = list(s1 - s2)
s4.sort()
print(len(s4))
for i in s4:
    print(i, end=' ')
