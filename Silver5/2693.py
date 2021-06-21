# N번째 큰 수

"""
2021/06/21 6:47 오후
정웅교
문제: https://www.acmicpc.net/problem/2693
"""
for _ in range(int(input())):
    ls = list(map(int, input().split()))
    ls.sort()
    print(ls[7])
