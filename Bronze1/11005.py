# 진법 변환 2

"""
2021/06/08 12:52 오후
정웅교
문제: https://www.acmicpc.net/problem/11005
"""
a, b = map(int, input().split())
ls = []
while a >= b:
    i = a % b
    if i >= 10:
        i += 55
        i = chr(i)
    ls.append(i)
    a = a // b
if a >= 10:
    a += 55
    a = chr(a)
ls.append(a)
for i in ls[::-1]:
    print(i, end='')
