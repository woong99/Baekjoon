# 줄 세우기

"""
2021/06/29 9:00 오후
정웅교
문제: https://www.acmicpc.net/problem/11536
"""
ls = []
for _ in range(int(input())):
    ls.append(input())
ls1 = sorted(ls)
ls2 = sorted(ls, reverse=True)

if ls == ls1:
    print('INCREASING')
elif ls == ls2:
    print('DECREASING')
else:
    print('NEITHER')
