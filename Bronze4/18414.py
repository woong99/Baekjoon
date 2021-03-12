# X に最も近い値

"""
2021/03/12 1:12 오후
정웅교
문제: https://www.acmicpc.net/problem/18414
"""

a, b, c = map(int, input().split())
ls = [a, b, c]
ls.sort()
print(ls[1])
