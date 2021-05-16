# 숫자의 합

"""
2021/05/17 1:11 오전
정웅교
문제: https://www.acmicpc.net/problem/11720
"""

n = int(input())
a = list(str(input()))
sum = 0
for i in a:
    sum += int(i)
print(sum)
