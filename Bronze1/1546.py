# 평균

"""
2021/05/28 1:40 오후
정웅교
문제: https://www.acmicpc.net/problem/1546
"""
n = int(input())
ls = list(map(int, input().split()))
ls1 = []
for i in ls:
    ls1.append(i / max(ls) * 100)

print(sum(ls1) / n)
