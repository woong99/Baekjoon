# Yangjojang of The Year

"""
2021/06/25 11:53 오후
정웅교
문제: https://www.acmicpc.net/problem/11557
"""
for _ in range(int(input())):
    ls = []
    for _ in range(int(input())):
        ls.append(list(map(str, input().split())))
    ls.sort(key=lambda x: int(x[1]))
    print(ls[len(ls) - 1][0])
