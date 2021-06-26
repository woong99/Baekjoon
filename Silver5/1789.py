# 수들의 합

"""
2021/06/26 11:40 오후
정웅교
문제: https://www.acmicpc.net/problem/1789
"""
s = int(input())
n = 1
while (n * (n + 1)) // 2 <= s:
    n += 1
print(n - 1)
