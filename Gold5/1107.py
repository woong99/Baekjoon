# 리모컨

"""
2022/01/18 1:46 오후
정웅교
문제: https://www.acmicpc.net/problem/1107
"""
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
if m == 0:
    ls = set()
else:
    ls = set(map(int, sys.stdin.readline().split()))
if n == 100:
    print(0)
else:
    ans = abs(100 - n)
    for i in range(1000001):
        stat = True
        for j in str(i):
            if int(j) in ls:
                stat = False
                break
        if stat:
            ans = min(len(str(i)) + abs(n - i), ans)
            # print(ans, i)
    print(ans)
