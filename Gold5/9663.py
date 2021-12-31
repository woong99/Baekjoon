# N-Queen

"""
2021/12/19 10:08 오후
정웅교
문제: https://www.acmicpc.net/problem/9663
"""
import math


def queens(i):
    global cnt
    # if i == n:
    #     cnt += 1
    #     for j in range(n + 1):
    #         col[j] = -1
    #     return
    # else:
    #     for j in range(1, n+1):
    #         col[i] = j
    #         print(f"q({i}) : {col}")
    #         print(f"queens({i + 1})")
    #         if promising(i):
    #             queens(i + 1)

    if promising(i):
        # print(f"promising({i})")
        if i == n:
            cnt += 1
            print(cnt)
            for i in range(n + 1):
                col[i] = -1;
        else:
            for j in range(1, n+1):
                col[i] = j
                print(f"q({i}) : {col}")
                print(f"queens({i + 1})")
                queens(i + 1)


def promising(i):
    if i == 1:
        return True
    for k in range(1, i):
        if col[i] == col[k] or abs(col[i] - col[k] == abs(i - k)):
            return False
    return True


n = int(input())
col = [-1 for _ in range(n + 1)]
cnt = 0
queens(1)
print(f"cnt={cnt}")
