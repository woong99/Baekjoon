# 연속부분최대곱

"""
2021/07/06 8:58 오후
정웅교
문제: https://www.acmicpc.net/problem/2670
"""

N = int(input())
li = [float(input()) for _ in range(N)]
for i in range(1, N):
    li[i] = max(li[i], li[i] * li[i - 1])
print("%.3f" % (max(li)))
