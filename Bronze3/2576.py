# 홀수

"""
2021/04/02 6:40 오후
정웅교
문제: https://www.acmicpc.net/problem/2576
"""
ls = []
for i in range(7):
    n = int(input())
    if n % 2 == 1:
        ls.append(n)
if not ls:
    print(-1)
else:
    print(sum(ls))
    print(min(ls))
