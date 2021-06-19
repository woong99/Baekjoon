# 소수

"""
2021/06/20 1:28 오전
정웅교
문제: https://www.acmicpc.net/problem/2581
"""


def sol(n):
    cnt = 0
    for i in range(2, n):
        if n % i == 0:
            cnt += 1
    if cnt == 0 and n != 1:
        return True
    elif n == 1:
        return False
    else:
        return False


a = int(input())
b = int(input())
ls = []
for i in range(a, b + 1):
    if sol(i):
        ls.append(i)
if len(ls) == 0:
    print(-1)
else:
    print(sum(ls))
    print(ls[0])
