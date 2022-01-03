# 부분수열의 합

"""
2022/01/02 3:27 오후
정웅교
문제: https://www.acmicpc.net/problem/1182
"""
import math


def sol(i):
    if i == k:
        if sum(arr) == s:
            if sorted(arr) not in ans:
                ans.append(sorted(arr))
    else:
        for j in range(n):
            if not visited[j]:
                arr[i] = ls[j]
                visited[j] = True
                sol(i + 1)
                visited[j] = False


n, s = map(int, input().split())
ls = list(map(int, input().split()))
cnt = 0
for k in range(1, n + 1):
    visited = [False for _ in range(n)]
    arr = [math.inf for _ in range(k)]
    ans = []
    sol(0)
    cnt += len(ans)
print(cnt)
