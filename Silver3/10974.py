# 모든 순열

"""
2021/08/15 9:36 오전
정웅교
문제: https://www.acmicpc.net/problem/10974
"""

n = int(input())
ls = [i for i in range(1, n + 1)]
ls1 = []


def sol():
    if len(ls1) == n:
        for i in ls1:
            print(i, end=' ')
        print()
        return
    for i in range(1, n + 1):
        if i in ls1:
            continue
        ls1.append(i)
        sol()
        ls1.pop()


sol()
