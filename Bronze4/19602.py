# Dog Treats

"""
2021/03/19 1:41 오후
정웅교
문제: https://www.acmicpc.net/problem/19602
"""
a = int(input())
b = int(input())
c = int(input())
sum = a + 2 * b + 3 * c
if sum < 10:
    print('sad')
else:
    print('happy')
