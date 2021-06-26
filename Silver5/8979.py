# 올림픽

"""
2021/06/27 12:07 오전
정웅교
문제: https://www.acmicpc.net/problem/8979
"""
a, b = map(int, input().split())
ls = []
for _ in range(a):
    ls.append(list(map(int, input().split())))
ls.sort(reverse=True, key=lambda x: (x[1], x[2], x[3]))
k, j, cnt = 1, 0, 0
for i in ls:
    if j > 0 and ls[j - 1][1:4] == i[1:]:
        i.append(k - 1)
        cnt += 1
    else:
        k += cnt
        i.append(k)
        k += 1
        cnt = 0
    j += 1
for i in ls:
    if i[0] == b:
        print(i[4])
