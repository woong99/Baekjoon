# 1, 2, 3 더하기 2

"""
2022/01/02 4:26 오후
정웅교
문제: https://www.acmicpc.net/problem/12101
"""


def sol(i, sum, ss):
    if sum == n:
        ls.append(ss[1:])

    for j in (1, 2, 3):
        if sum < n:
            sum += j
            sol(i + 1, sum, ss + '+' + str(j))
            sum -= j


n, k = map(int, input().split())
s = ''
ls = []
sol(0, 0, s)
ls.sort()
if k > len(ls):
    print(-1)
else:
    print(ls[k - 1])
