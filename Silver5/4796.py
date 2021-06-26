# 캠핑

"""
2021/06/26 11:46 오후
정웅교
문제: https://www.acmicpc.net/problem/4796
"""
import sys

input = sys.stdin.readline

cnt = 1
while 1:
    l, p, v = map(int, input().split())
    if l + p + v == 0:
        break

    res = (v // p) * l
    res += min((v % p), l)
    print('Case %d: %d' % (cnt, res))
    cnt += 1
