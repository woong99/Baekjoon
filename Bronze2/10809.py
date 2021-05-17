# 알파벳 찾기

"""
2021/05/17 3:07 오전
정웅교
문제: https://www.acmicpc.net/problem/10809
"""
ls = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
      'x', 'y', 'z']
n = str(input())
for i in range(len(n)):
    for k in ls:
        if k == n[i]:
            ls[ls.index(k)] = i
for i in range(len(ls)):
    if type(ls[i]) == str:
        ls[i] = -1
for i in ls:
    print(i, end=' ')
