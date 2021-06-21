# K번째 수

"""
2021/06/21 6:04 오후
정웅교
문제: https://www.acmicpc.net/problem/11004
"""
a, b = map(int, input().split())
ls = list(map(int, input().split()))
ls.sort()
print(ls[b - 1])
