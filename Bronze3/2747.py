# 피보나치 수

"""
2021/04/02 6:58 오후
정웅교
문제: https://www.acmicpc.net/problem/2747
"""

n = int(input())
ls = [0, 1]
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    for i in range(2, n + 1):
        ls.append(ls[i - 2] + ls[i - 1])
    print(ls[n])
