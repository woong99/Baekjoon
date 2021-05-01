# 전투 드로이드 가격

"""
2021/05/01 10:56 오후
정웅교
문제: https://www.acmicpc.net/problem/5361
"""

n = int(input())
for _ in range(n):
    a, b, c, d, e = map(int, input().split())
    sum = a * 350.34 + b * 230.90 + c * 190.55 + d * 125.30 + e * 180.90
    print('$' + format(sum, '.2f'))
