# 수 이어 쓰기 1

"""
2021/08/15 2:39 오후
정웅교
문제: https://www.acmicpc.net/problem/1748
"""
n = int(input())
s = 0
while 1:
    d = len(str(n))
    k = n - 10 ** (d - 1) + 1
    s += k * d
    n -= k
    if n == 0:
        break
print(s)
