# 크냐?

"""
2021/04/11 12:24 오전
정웅교
문제: https://www.acmicpc.net/problem/4101
"""
while 1:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    if a > b:
        print('Yes')
    else:
        print('No')
