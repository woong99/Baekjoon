# 듣보잡

"""
2021/07/19 11:48 오전
정웅교
문제: https://www.acmicpc.net/problem/1764
"""

a, b = map(int, input().split())
ls1 = set()
ls2 = set()
for _ in range(a):
    ls1.add(input())
for _ in range(b):
    ls2.add(input())
ls3 = list(ls1 & ls2)
ls3.sort()
print(len(ls3))
for i in ls3:
    print(i)
