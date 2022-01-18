# 1

"""
2022/01/18 12:54 오후
정웅교
문제: https://www.acmicpc.net/problem/4375
"""
try:
    while True:
        n = int(input())
        i = 1
        while True:
            if i % n == 0:
                break
            i = i * 10 + 1
        print(len(str(i)))
except:
    exit()
