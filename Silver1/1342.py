# 행운의 문자열

"""
2022/01/02 2:34 오후
정웅교
문제: https://www.acmicpc.net/problem/1342
"""


def sol(i):
    if i == n:
        t = ''.join(arr)
        ans.add(t)
    else:
        for j in range(n):
            if not visited[j]:
                arr[i] = s[j]
                if i == 0:
                    visited[j] = True
                    sol(i + 1)
                    visited[j] = False
                else:
                    if i > 0 and arr[i] != arr[i - 1]:
                        visited[j] = True
                        sol(i + 1)
                        visited[j] = False


s = input()
n = len(s)
visited = [False for _ in range(n)]
arr = ['*' for _ in range(n)]
ans = set()
sol(0)
print(len(ans))
