# 파도반 수열

"""
2021/08/14 10:34 오전
정웅교
문제: https://www.acmicpc.net/problem/9461
"""

for _ in range(int(input())):
    ls = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    n = int(input())
    for i in range(10, n + 1):
        ls.append(ls[i - 3] + ls[i - 2])
    print(ls[n - 1])
