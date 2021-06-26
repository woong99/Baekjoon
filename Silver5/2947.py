# 나무 조각

"""
2021/06/27 1:26 오전
정웅교
문제: https://www.acmicpc.net/problem/2947
"""


def sol():
    for i in ls:
        print(i, end=' ')
    print()


ls = list(map(int, input().split()))
while 1:
    if ls[0] > ls[1]:
        ls[0], ls[1] = ls[1], ls[0]
        sol()
    if ls[1] > ls[2]:
        ls[1], ls[2] = ls[2], ls[1]
        sol()
    if ls[2] > ls[3]:
        ls[2], ls[3] = ls[3], ls[2]
        sol()
    if ls[3] > ls[4]:
        ls[3], ls[4] = ls[4], ls[3]
        sol()
    if ls == [1, 2, 3, 4, 5]:
        break
