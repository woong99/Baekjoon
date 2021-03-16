# Alex Origami Squares

"""
2021/03/16 1:00 오후
정웅교
문제: https://www.acmicpc.net/problem/11466
"""

a, b = map(int, input().split())

if a < b:
    temp = a
    a = b
    b = temp
if a > b * 3:
    print(b)
elif a > b * 1.5:
    print(a / 3)
else:
    print(b / 2)
