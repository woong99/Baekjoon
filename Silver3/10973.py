# 이전 순열

"""
2021/08/15 3:50 오후
정웅교
문제: https://www.acmicpc.net/problem/10973
"""
n = int(input())
ls = list(map(int, input().split()))
ls1 = []
for i in ls:
    ls1.append(i)
ls1.sort()
if ls == ls1:
    print(-1)
else:
    j = len(ls) - 1
    i = len(ls) - 1
    while 1:
        if ls[i - 1] > ls[i]:
            if ls[i - 1] < ls[j]:
                j -= 1
                continue
            ls[j], ls[i - 1] = ls[i - 1], ls[j]
            ls_sep1 = ls[i:]
            ls = ls[:i]
            ls_sep1.sort(reverse=True)
            ls.extend(ls_sep1)
            break
        else:
            i -= 1
    for i in ls:
        print(i, end=' ')
