# 로또

"""
2021/09/02 4:58 오후
정웅교
문제: https://www.acmicpc.net/problem/6603
"""


def sol(i):
    if i == 6:
        s = ' '.join(sorted(arr, key=int))
        if s not in ans:
            print(s)
        ans.add(s)
    else:
        for j in range(n):
            if not visited[j]:
                arr[i] = ls[j]
                visited[j] = True
                sol(i + 1)
                visited[j] = False


while 1:
    ls = list(map(str, input().split()))
    if len(ls) == 1 and ls[0] == '0':
        break
    n = int(ls[0])
    del (ls[0])
    visited = [False for _ in range(n)]
    arr = [-1 for _ in range(6)]
    ans = set()
    sol(0)
    print()
