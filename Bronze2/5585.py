# 거스름돈

"""
2021/05/19 2:39 오후
정웅교
문제: https://www.acmicpc.net/problem/5585
"""

n = 1000 - int(input())
cnt = 0
while n > 0:
    if n >= 500:
        cnt += 1
        n -= 500
    elif 500 > n >= 100:
        cnt += 1
        n -= 100
    elif 100 > n >= 50:
        cnt += 1
        n -= 50
    elif 50 > n >= 10:
        cnt += 1
        n -= 10
    elif 10 > n >= 5:
        cnt += 1
        n -= 5
    else:
        cnt += 1
        n -= 1
print(cnt)
