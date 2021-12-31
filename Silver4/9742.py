# 순열

"""
2021/12/31 8:43 오후
정웅교
문제: https://www.acmicpc.net/problem/9742
"""


def sol(i):
    global cnt
    if i == n:
        cnt += 1
        if cnt == int(b):
            for k in ls:
                t.append(k)
    else:
        for j in range(n):
            if not visited[j]:
                visited[j] = True
                ls[i] = a[j]
                sol(i + 1)
                visited[j] = False


try:
    while 1:
        a, b = map(str, input().split())
        n = len(a)
        ls = [-1 for _ in range(n)]
        visited = [False for _ in range(n)]
        cnt = 0
        t = []
        sol(0)
        if len(t) == 0:
            print(f"{a} {b} = No permutation", end="")
        else:
            print(f"{a} {b} = ", end="")
            for k in t:
                print(k, end="")
        print()
except:
    exit()
