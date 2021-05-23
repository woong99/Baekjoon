# 과제 안 내신 분..?

"""
2021/05/23 12:46 오후
정웅교
문제: https://www.acmicpc.net/problem/5597
"""
ls = list()
ls1 = list()
for _ in range(28):
    ls.append(int(input()))
for i in range(1, 31):
    ls1.append(i)
ls.sort()
for i in ls:
    for k in ls1:
        if i == k:
            ls1.remove(k)
print(ls1[0])
print(ls1[1])
