# 좌표 정렬하기 2

"""
2021/06/20 11:41 오후
정웅교
문제: https://www.acmicpc.net/problem/11651
"""
ls = []
for _ in range(int(input())):
    a = list(map(int, input().split()))
    ls.append(a)
ls.sort(key=lambda x: (x[1], x[0]))
for i in ls:
    for k in i:
        print(k, end=' ')
    print()
