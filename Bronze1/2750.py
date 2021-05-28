# 수 정렬하기

"""
2021/05/28 1:59 오후
정웅교
문제: https://www.acmicpc.net/problem/2750
"""
ls = []
for _ in range(int(input())):
    ls.append(int(input()))
ls.sort()
for i in ls:
    print(i)
