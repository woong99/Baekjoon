# 대표값 2

"""
2021/05/23 1:12 오후
정웅교
문제: https://www.acmicpc.net/problem/2587
"""

ls = list()
for _ in range(5):
    ls.append(int(input()))
ls.sort()
print(sum(ls) // 5)
print(ls[2])
