# 스타후르츠

"""
2021/02/25 5:41 오후
정웅교
문제: https://www.acmicpc.net/problem/17496
"""

n, t, c, p = map(int, input().split())
cnt = 0
day = 1
while 1:
    day += t
    if day > n:
        break
    cnt += 1
print(cnt * c * p)
