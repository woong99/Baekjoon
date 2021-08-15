# 다음 순열

"""
2021/08/15 11:33 오전
정웅교
문제: https://www.acmicpc.net/problem/10972
"""
n = int(input())
ls = list(map(int, input().split()))
if n != 1:
    ls5 = ls
    j = len(ls) - 1
    i = len(ls) - 1
    while 1:
        if ls[i - 1] < ls[i]:
            if ls[i - 1] > ls[j]:
                j -= 1
                continue
            ls[i - 1], ls[j] = ls[j], ls[i - 1]
            ls1 = ls[i:]
            ls = ls[:i]
            ls1.sort()
            ls.extend(ls1)
            break
        else:
            i -= 1
    ls5.sort()
    if ls == ls5:
        print(-1)
    else:
        for k in ls:
            print(k, end=' ')
else:
    print(-1)
