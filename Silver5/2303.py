# 숫자 게임

"""
2021/06/28 11:02 오후
정웅교
문제: https://www.acmicpc.net/problem/2303
"""
import itertools

ls2 = []
for _ in range(int(input())):
    ls = list(map(int, input().split()))
    ls = list(itertools.combinations(ls, 3))
    ls1 = []
    for i in ls:
        s = str(sum(i))
        ls1.append(s[len(s) - 1])
    ls2.append(max(ls1))
max = 0
cnt = 0
for i in range(len(ls2)):
    if int(ls2[i]) >= max:
        max = int(ls2[i])
        cnt = i + 1
print(cnt)
