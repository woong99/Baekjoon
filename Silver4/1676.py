# 팩토리얼 0의 개수

"""
2021/07/03 8:28 오후
정웅교
문제: https://www.acmicpc.net/problem/1676
"""


def fac(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    res = 1
    for i in range(n, 1, -1):
        res *= i
    return res


n = int(input())
s = list(str(fac(n)))
cnt = 0
for _ in range(len(s)):
    k = s.pop()
    if k == '0':
        cnt += 1
    else:
        break
print(cnt)
