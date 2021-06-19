# 좌표 정렬하기

"""
2021/06/20 1:36 오전
정웅교
문제: https://www.acmicpc.net/problem/11650
"""
ls = []
for _ in range(int(input())):
    ls.append(list(map(int, input().split())))
ls.sort()
for i in ls:
    print(i[0], i[1])
