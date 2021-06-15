# 첼시를 도와줘!

"""
2021/06/15 2:35 오후
정웅교
문제: https://www.acmicpc.net/problem/11098
"""
for _ in range(int(input())):
    ls = []
    ls1 = []
    n = int(input())
    for _ in range(n):
        a = list(map(str, input().split()))
        ls.append(a)
    for i in range(n):
        ls1.append(int(ls[i][0]))
    i = max(ls1)
    print(ls[ls1.index(i)][1])
