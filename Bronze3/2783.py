# 삼각 김밥

"""
2021/04/03 2:08 오후
정웅교
문제: https://www.acmicpc.net/problem/2783
"""

ls = []
a, b = map(float, input().split())
ls.append(a * 1000 / b)
n = int(input())
for i in range(n):
    c, d = map(float, input().split())
    ls.append(c * 1000 / d)
print(round(min(ls), 2))
