# 문자열 분석

"""
2021/05/21 1:28 오후
정웅교
문제: https://www.acmicpc.net/problem/10820
"""

try:
    while True:
        a = input()
        sum1, sum2, sum3, sum4 = 0, 0, 0, 0
        for i in a:
            if i.isdigit():
                sum3 += 1
            elif i == ' ':
                sum4 += 1
            elif i.isupper():
                sum2 += 1
            else:
                sum1 += 1
        print(sum1, sum2, sum3, sum4)
except:
    exit()
