# 짝수를 찾아라

"""
2021/04/06 1:46 오후
정웅교
문제: https://www.acmicpc.net/problem/3058
"""

t = int(input())
for _ in range(t):
    a = list(map(int, input().split()))
    sum = 0
    ls = []
    for i in a:
        if i % 2 == 0:
            sum += i
            ls.append(i)
    ls.sort()
    print(sum, ls[0])
