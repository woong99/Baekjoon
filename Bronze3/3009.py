# 네 번쨰 점

"""
2021/05/13 3:51 오후
정웅교
문제: https://www.acmicpc.net/problem/3009
"""

a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
a3, b3 = map(int, input().split())
cnt1 = 0
cnt2 = 0
a = 0
b = 0
ls1 = [a1, a2, a3]
ls2 = [b1, b2, b3]
ls1.sort()
ls2.sort()
c = ls1[0]
d = ls2[0]
for i in ls1:
    if c == i:
        cnt1 += 1
if cnt1 == 2:
    a = ls1[2]
else:
    a = ls1[0]
for i in ls2:
    if d == i:
        cnt2 += 1
if cnt2 == 2:
    b = ls2[2]
else:
    b = ls2[0]
print(a, b)
