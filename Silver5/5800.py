# 성적 통계

"""
2021/06/22 5:20 오후
정웅교
문제: https://www.acmicpc.net/problem/5800
"""
for i in range(int(input())):
    ls = list(map(int, input().split()))[1:]
    ls.sort()
    ls1 = []
    for k in range(len(ls) - 1):
        ls1.append(ls[k + 1] - ls[k])
    print(f"Class {i + 1}")
    print(f"Max {max(ls)}, Min {min(ls)}, Largest gap {max(ls1)}")
