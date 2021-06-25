# 회사에 있는 사람

"""
2021/06/25 11:29 오후
정웅교
문제: https://www.acmicpc.net/problem/7785
"""
ls = []
for _ in range(int(input())):
    a, b = map(str, input().split())
    if b == 'enter':
        ls.append(a)
    else:
        ls.remove(a)
ls.sort(reverse=True)
print('\n'.join(ls))
