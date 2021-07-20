# 요세푸스 문제 0

"""
2021/07/20 10:59 오전
정웅교
문제: https://www.acmicpc.net/problem/11866
"""
a, b = map(int, input().split())
ls = [i for i in range(1, a + 1)]
print('<', end='')
i = b - 1
while len(ls) > 1:
    print(ls[i], end=', ')
    del (ls[i])
    i += b - 1
    i %= len(ls)
print(f"{ls[0]}>")
