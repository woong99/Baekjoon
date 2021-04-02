# 세탁소 사장 동혁

"""
2021/04/02 6:43 오후
정웅교
문제: https://www.acmicpc.net/problem/2720
"""

n = int(input())
for i in range(n):
    k = int(input())
    print(k // 25, k % 25 // 10, k % 25 % 10 // 5, k % 25 % 10 % 5)
