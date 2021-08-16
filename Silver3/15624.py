# 피보나치 수 7

"""
2021/08/16 1:13 오후
정웅교
문제: https://www.acmicpc.net/problem/15624
"""
n = int(input())
ls = [0, 1, 1, 2]
for i in range(4, n + 1):
    ls.append((ls[i - 2] + ls[i - 1]) % 1000000007)
print(ls[n])
