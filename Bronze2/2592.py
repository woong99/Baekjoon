# 대표값

"""
2021/05/24 4:11 오후
정웅교
문제: https://www.acmicpc.net/problem/2592
"""

ls = list()
for _ in range(10):
    ls.append(int(input()))
ls1 = list(set(ls))
ls2 = [0 for i in range(len(ls1))]
for i in range(len(ls1)):
    cnt = 0
    for k in ls:
        if k == ls1[i]:
            cnt += 1
    ls2[i] = cnt
print(sum(ls) // 10)
print(ls1[ls2.index(max(ls2))])
