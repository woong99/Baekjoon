# 뒤집힌 덧셈

"""
2021/05/31 3:21 오후
정웅교
문제: https://www.acmicpc.net/problem/1357
"""
a, b = map(str, input().split())
a = a[::-1]
b = b[::-1]
sum = str(int(a) + int(b))
sum = sum[::-1]
print(int(sum))
