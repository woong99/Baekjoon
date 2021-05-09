# 내 학점을 구해줘

"""
2021/05/09 5:32 오후
정웅교
문제: https://www.acmicpc.net/problem/10984
"""
n = int(input())
for _ in range(n):
    a = int(input())
    sum1 = 0
    sum2 = 0
    for _ in range(a):
        a, b = map(float, input().split())
        sum1 += a
        sum2 += a * b
    print(int(sum1), format(sum2 / sum1, '.1f'))
