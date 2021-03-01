# 과목선택

"""
2021/03/01 4:39 오후
정웅교
문제: https://www.acmicpc.net/problem/11948
"""

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

ls1 = [a, b, c, d]
ls1.sort()
sum = 0
for i in range(1, 4):
    sum += ls1[i]
if e < f:
    sum += f
else:
    sum += e
print(sum)
