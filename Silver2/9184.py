# 신나는 함수 실행

"""
2022/01/14 2:17 오후
정웅교
문제: https://www.acmicpc.net/problem/9184
"""
dp = [[[1 for _ in range(21)] for _ in range(21)] for _ in range(21)]
for i in range(1, 21):
    for j in range(1, 21):
        for k in range(1, 21):
            dp[i][j][k] = dp[i - 1][j][k] + dp[i - 1][j - 1][k] + dp[i - 1][j][k - 1] - dp[i - 1][j - 1][k - 1]
while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    elif a <= 0 or b <= 0 or c <= 0:
        print(f'w({a}, {b}, {c}) = 1')
    else:
        if a > 20 or b > 20 or c > 20:
            print(f'w({a}, {b}, {c}) = {dp[20][20][20]}')
        else:
            print(f'w({a}, {b}, {c}) = {dp[a][b][c]}')
