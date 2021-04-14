# 배수 찾기

"""
2021/04/12 4:26 오후
정웅교
문제: https://www.acmicpc.net/problem/4504
"""
k = int(input())
while 1:
    i = int(input())
    if i == 0:
        break
    if i % k == 0:
        print(f"{i} is a multiple of {k}.")
    else:
        print(f"{i} is NOT a multiple of {k}.")
