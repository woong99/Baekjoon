# 지영 공주님의 마법 거울

"""
2021/06/19 12:42 오전
정웅교
문제: https://www.acmicpc.net/problem/11586
"""
n = int(input())
ls = []
for _ in range(n):
    ls.append(list(map(str, input().split())))
k = int(input())
if k == 1:
    for i in ls:
        for j in i:
            print(j, end='')
        print()
elif k == 2:
    for i in ls:
        print(i[0][::-1])
    print()
else:
    for i in ls[::-1]:
        print(i[0])
    print()
