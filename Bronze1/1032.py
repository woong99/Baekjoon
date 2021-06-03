# 명령 프롬프트

"""
2021/06/03 5:52 오후
정웅교
문제: https://www.acmicpc.net/problem/1032
"""
ls = []
n = int(input())
for _ in range(n):
    ls.append(input())
for i in range(len(ls[0])):
    ls1 = []
    for k in range(n):
        ls1.append(ls[k][i])
    if len(list(set(ls1))) == 1:
        print(list(set(ls1))[0], end='')
    else:
        print('?', end='')
print()
