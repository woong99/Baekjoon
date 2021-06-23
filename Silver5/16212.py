# 정열적인 정렬

"""
2021/06/23 8:24 오후
정웅교
문제: https://www.acmicpc.net/problem/16212
"""

n = int(input())
ls = list(map(int, input().split()))
ls.sort()
print(*ls, sep=' ')
