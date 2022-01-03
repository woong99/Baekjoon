# 부등호

"""
2022/01/03 10:06 오전
정웅교
문제: https://www.acmicpc.net/problem/2529
"""


def sol(i):
    if i == n + 1:
        ans.append(''.join(s))
    else:
        for j in range(10):
            if not visited[j]:
                if i > 0 and ls[i - 1] == '<':
                    if j > int(s[i - 1]):
                        s[i] = str(j)
                        visited[j] = True
                        sol(i + 1)
                        visited[j] = False
                elif i > 0 and ls[i - 1] == '>':
                    if j < int(s[i - 1]):
                        s[i] = str(j)
                        visited[j] = True
                        sol(i + 1)
                        visited[j] = False
                else:
                    s[i] = str(j)
                    visited[j] = True
                    sol(i + 1)
                    visited[j] = False


n = int(input())
ls = list(map(str, input().split()))
s = [-1 for _ in range(n + 1)]
visited = [False for _ in range(10)]
ans = []
sol(0)
print(ans[len(ans) - 1])
print(ans[0])
