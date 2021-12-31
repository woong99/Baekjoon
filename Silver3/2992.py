# 크면서 작은 수

"""
2021/12/31 9:41 오후
정웅교
문제: https://www.acmicpc.net/problem/2992
"""


def sol(i):
    if i == n:
        t = ''.join(ls)
        if int(s) < int(t):
            ls1.append(t)

    else:
        for j in range(n):
            if not visited[j]:
                ls[i] = s1[j]
                visited[j] = True
                sol(i + 1)
                visited[j] = False


s = input()
s1 = ''.join(sorted(s))
n = len(s)
ls = [-1 for _ in range(n)]
ls1 = []
visited = [False for _ in range(n)]
sol(0)
if len(ls1) == 0:
    print(0)
else:
    print(ls1[0])
