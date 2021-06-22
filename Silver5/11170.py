# 0의 개수

"""
2021/06/22 6:03 오후
정웅교
문제: https://www.acmicpc.net/problem/11170
"""
for _ in range(int(input())):
    a, b = map(int, input().split())
    cnt = 0
    for i in range(a, b + 1):
        cnt += str(i).count('0')
    print(cnt)
