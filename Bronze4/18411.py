# 試験

"""
2021/03/12 1:13 오후
정웅교
문제: https://www.acmicpc.net/problem/18411
"""

a, b, c = map(int, input().split())
ls = [a, b, c]
ls.sort()
print(ls[1] + ls[2])
