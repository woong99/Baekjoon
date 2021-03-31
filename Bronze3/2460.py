# 지능형 기차 2

"""
2021/03/31 2:17 오후
정웅교
문제: https://www.acmicpc.net/problem/2460
"""
ls1 = []
ls2 = []
ls3 = []
sum = 0

for i in range(10):
    a, b = map(int, input().split())
    ls1.append(a)
    ls2.append(b)
for i in range(10):
    sum -= ls1[i]
    sum += ls2[i]
    ls3.append(sum)
ls3.sort()
print(ls3[9])
