# 평균 점수

"""
2021/02/25 9:57 오후
정웅교
문제: https://www.acmicpc.net/problem/10039
"""

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if a < 40:
    a = 40
if b < 40:
    b = 40
if c < 40:
    c = 40
if d < 40:
    d = 40
if e < 40:
    e = 40
sum = a + b + c + d + e
print(sum // 5)
