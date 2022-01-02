# 차이를 최대로

"""
2022/01/02 2:17 오후
정웅교
문제: https://www.acmicpc.net/problem/10819
"""


def sol(i):
    if i == n:
        sum = 0
        for k in range(n - 1):
            sum += abs(arr[k] - arr[k + 1])
            ans.append(sum)
    else:
        for j in range(n):
            if not visited[j]:
                arr[i] = ls[j]
                visited[j] = True
                sol(i + 1)
                visited[j] = False


n = int(input())
ls = list(map(int, input().split()))
arr = [-1 for _ in range(n)]
visited = [False for _ in range(n)]
ans = []
sol(0)
print(max(ans))
