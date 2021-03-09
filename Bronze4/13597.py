# Tri-du

"""
2021/03/09 5:45 오후
정웅교
문제: https://www.acmicpc.net/problem/13597
"""
a, b = map(int, input().split())
if a != b:
    if a < b:
        print(b)
    else:
        print(a)
else:
    print(a)
