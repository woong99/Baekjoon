# 수 정렬하기 2

"""
2021/06/19 5:11 오전
정웅교
문제: https://www.acmicpc.net/problem/2751
"""
ls = []
for _ in range(int(input())):
    ls.append(int(input()))
ls.sort()
for i in ls:
    print(i)
