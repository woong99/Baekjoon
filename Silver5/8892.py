# 팰린드롬

"""
2021/06/24 10:28 오후
정웅교
문제: https://www.acmicpc.net/problem/8892
"""
import itertools

for _ in range(int(input())):
    ls = []
    for _ in range(int(input())):
        ls.append(input())
    s = list(itertools.permutations(ls, 2))
    cnt = 0
    for i in range(len(s)):
        k = s[i][0] + s[i][1]
        if k == k[::-1]:
            print(k)
            cnt += 1
            break
    if cnt == 0:
        print(0)
