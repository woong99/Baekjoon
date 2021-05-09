# A+B-5

"""
2021/05/09 5:30 오후
정웅교
문제: https://www.acmicpc.net/problem/10952
"""

while 1:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    print(a + b)
