# 지능형 기차

"""
2021/03/31 2:14 오후
정웅교
문제: https://www.acmicpc.net/problem/2455
"""

a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
a3, b3 = map(int, input().split())
a4, b4 = map(int, input().split())
ls1 = [a1, a2, a3, a4]
ls2 = [b1, b2, b3, b4]
ls3 = []
sum = 0
for i in range(4):
    sum -= ls1[i]
    sum += ls2[i]
    ls3.append(sum)
ls3.sort()
print(ls3[3])
