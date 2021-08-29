# 다이나믹이 뭐예요?

"""
2021/08/29 3:35 오후
정웅교
문제: https://www.acmicpc.net/problem/14494
"""
n, m = map(int, input().split())
ls = [[0 for i in range(n)] for i in range(m)]
for i in range(m):
    for j in range(n):
        if i == 0 or j == 0:
            ls[i][j] = 1
        else:
            ls[i][j] = (ls[i - 1][j] + ls[i][j - 1] + ls[i - 1][j - 1]) % 1000000007
print(ls[m - 1][n - 1])
