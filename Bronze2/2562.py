# 최댓값

"""
2021/05/17 2:15 오전
정웅교
문제: https://www.acmicpc.net/problem/2562
"""
ls = list()
for _ in range(9):
    ls.append(int(input()))
print(max(ls))
print(ls.index(max(ls)) + 1)
