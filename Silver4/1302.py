# 베스트셀러

"""
2021/08/09 10:31 오전
정웅교
문제: https://www.acmicpc.net/problem/1302
"""
ls = []
dic = {}
for _ in range(int(input())):
    ls.append(input())
ls.sort()
dic[ls[0]] = 1
for i in range(1, len(ls)):
    if ls[i] == ls[i - 1]:
        dic[ls[i]] += 1
    else:
        dic[ls[i]] = 1
for key, value in dic.items():
    if value == max(list(dic.values())):
        print(key)
        break
