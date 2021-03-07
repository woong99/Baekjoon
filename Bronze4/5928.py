# Contest Timing

"""
2021/03/07 10:56 오전
정웅교
문제: https://www.acmicpc.net/problem/5928
"""
a, b, c = map(int, input().split())
n1 = a * 24 * 60 + b * 60 + c
n2 = 11 * 24 * 60 + 11 * 60 + 11
if n1 < n2 or a < 11:
    print(-1)
else:
    print(n1 - n2)
