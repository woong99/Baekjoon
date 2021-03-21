# 2 番目に大きい整数

"""
2021/03/21 3:00 오후
정웅교
문제: https://www.acmicpc.net/problem/20976
"""
a, b, c = map(int, input().split())
ls = [a, b, c]
ls.sort()
print(ls[1])
