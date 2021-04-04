# 나는 요리사다

"""
2021/04/04 3:09 오후
정웅교
문제: https://www.acmicpc.net/problem/2953
"""
ls = []
for i in range(5):
    a = list(map(int, input().split()))
    ls.append(sum(a))
print(ls.index(max(ls)) + 1, max(ls))
