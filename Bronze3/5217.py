# 쌍의 합

"""
2021/05/01 10:21 오후
정웅교
문제: https://www.acmicpc.net/problem/5217
"""

n = int(input())
for _ in range(n):
    i = int(input())
    t = i // 2
    ls = []
    for k in range(1, t + 1):
        if k != i - k:
            ls.append(k)
            ls.append(i - k)
    if len(ls) <= 2:
        print(f"Pairs for {i}: ", end="")
        for q in range(len(ls)):
            print(f"{ls[q]} ", end="")
        print()
    else:
        print(f"Pairs for {i}:", end="")
        cnt = 0
        for q in range(len(ls)):
            print(f" {ls[q]}", end="")
            cnt += 1
            if cnt % 2 == 0 and q != len(ls) - 1:
                print(f",", end="")
        print()
