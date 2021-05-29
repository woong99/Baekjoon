# 단어 뒤집기

"""
2021/05/29 7:46 오후
정웅교
문제: https://www.acmicpc.net/problem/9093
"""
for _ in range(int(input())):
    s = list(map(str, input().split(' ')))
    for i in s:
        print(i[::-1], end=' ')
    print()
