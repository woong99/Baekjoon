# 중복 빼고 정렬하기

"""
2021/06/21 6:41 오후
정웅교
문제: https://www.acmicpc.net/problem/10867
"""

n = int(input())
ls = list(set(map(int, input().split())))
ls.sort()
for i in ls:
    print(i, end=' ')
