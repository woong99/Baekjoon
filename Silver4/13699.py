# 점화식

"""
2021/08/07 11:57 오전
정웅교
문제: https://www.acmicpc.net/problem/13699
"""

n = int(input())
t = [1, 1, 2, 5]
sum = 0
if n <= 3:
    print(t[n])
else:
    for i in range(4, n + 1):
        for k in range(i):
            sum += t[k] * t[i - k - 1]
        t.append(sum)
        sum = 0
    print(t[n])
