# 암기왕

"""
2021/08/09 10:45 오전
정웅교
문제: https://www.acmicpc.net/problem/2776
"""


def binary_search(tar, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2
        if data[mid] == tar:
            return True
        elif data[mid] < tar:
            start = mid + 1
        else:
            end = mid - 1
    return False


for _ in range(int(input())):
    n1 = int(input())
    ls1 = list(map(int, input().split()))
    n2 = int(input())
    ls2 = list(map(int, input().split()))
    ls1.sort()
    for i in ls2:
        if binary_search(i, ls1):
            print(1)
        else:
            print(0)
