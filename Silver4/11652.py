# 카드

"""
2021/08/07 11:40 오전
정웅교
문제: https://www.acmicpc.net/problem/11652
"""
dic = {}
ls = []
for _ in range(int(input())):
    ls.append(int(input()))
ls.sort()
dic[ls[0]] = 1
for i in range(1, len(ls)):
    if ls[i] != ls[i - 1]:
        dic[ls[i]] = 1
    else:
        dic[ls[i]] += 1
ls1 = list(dic.values())

for key, value in dic.items():
    if max(ls1) == value:
        print(key)
        break
