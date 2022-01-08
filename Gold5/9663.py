# N-Queen

"""
2021/12/19 10:08 오후
정웅교
문제: https://www.acmicpc.net/problem/9663
"""


def queens(i):
    global cnt
    print(col, i)
    # if promising(i):

    if i == n - 1:
        # print(col)
        cnt += 1
    else:
        for j in range(n):
            col[i] = j
            print(f"q({i + 1})")
            queens(i + 1)
            col[i] = -1


def promising(i):
    # print(col, i)
    if i == 0:
        return True
    for k in range(0, i):
        # print(f"col[{i}]({col[i]}) == col[{k}]({col[k]})")
        if col[i] == col[k] or abs(col[i] - col[k] == abs(i - k)):
            # print(False)
            return False
    return True


n = int(input())
col = [-1 for _ in range(n)]
cnt = 0
queens(0)
print(f"cnt={cnt}")
