# 숫자의 개수

"""
2021/05/17 12:54 오전
정웅교
문제: https://www.acmicpc.net/problem/2577
"""

a = int(input())
b = int(input())
c = int(input())
result = list(str(a * b * c))
for i in range(10):
    print(result.count(str(i)))
