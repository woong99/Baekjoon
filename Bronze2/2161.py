# 카드1

"""
2021/05/24 3:40 오후
정웅교
문제: https://www.acmicpc.net/problem/2161
"""

n = int(input())
ls = list(range(1, n + 1))
ls1 = []
cnt = 0
while len(ls) >= 1:
    if cnt % 2 == 0:
        ls1.append(ls[0])
        ls.remove(ls[0])
        cnt += 1
    else:
        ls.append(ls[0])
        ls.remove(ls[0])
        cnt += 1
for i in ls1:
    print(i, end=' ')
