# 꼬리를 무는 숫자 나열

"""
2021/03/26 6:09 오후
정웅교
문제: https://www.acmicpc.net/problem/1598
"""
from math import ceil

a, b = map(int, input().split())

print(abs((ceil(a / 4) * 4 - a) - (ceil(b / 4) * 4 - b)) + abs((ceil(a / 4) * 4) - (ceil(b / 4) * 4)) // 4)
