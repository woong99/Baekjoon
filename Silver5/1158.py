# 요세푸스 문제

"""
2021/06/20 1:48 오전
정웅교
문제: https://www.acmicpc.net/problem/1158
"""
a, b = map(int, input().split())
ls = list(range(1, a + 1))
ls1 = []
i = b - 1
while len(ls) > 1:
    ls1.append(ls[i])
    ls.remove(ls[i])
    if i + b - 1 >= len(ls):
        i = (i + b - 1) % len(ls)
    else:
        i += b - 1
print('<', end='')
for i in ls1:
    print(f"{i}, ", end='')
print(f"{ls[0]}>")
