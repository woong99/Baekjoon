# 열 개씩 끊어 출력하기

"""
2021/05/18 10:32 오후
정웅교
문제: https://www.acmicpc.net/problem/11721
"""

n = str(input())
for i in range(len(n)):
    print(n[i], end='')
    if i % 10 == 9:
        print()
