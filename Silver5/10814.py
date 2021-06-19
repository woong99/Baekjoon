# 나이순 정렬

"""
2021/06/20 2:15 오전
정웅교
문제: https://www.acmicpc.net/problem/10814
"""
ls = []
for i in range(int(input())):
    a, b = input().split()
    ls1 = [int(a), b, i]
    ls.append(ls1)
ls.sort(key=lambda x: (x[0], x[2]))
for i in ls:
    print(i[0], i[1])
