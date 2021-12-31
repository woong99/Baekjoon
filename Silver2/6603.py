# 로또

"""
2021/09/02 4:58 오후
정웅교
문제: https://www.acmicpc.net/problem/6603
"""
while 1:
    s = set(map(int, input().split()))
    if len(s) == 1 and s[0] == 0:
        break
    print(s)
