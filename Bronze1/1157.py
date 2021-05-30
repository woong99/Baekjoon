# 단어 공부

"""
2021/05/30 10:27 오전
정웅교
문제: https://www.acmicpc.net/problem/1157
"""
s = input().upper()
s1 = list(set(s))
ls = []
for i in s1:
    ls.append(s.count(i))
n = max(ls)
if ls.count(n) != 1:
    print('?')
else:
    print(s1[ls.index(n)])
