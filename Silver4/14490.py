# 백대열

"""
2021/08/06 1:16 오후
정웅교
문제: https://www.acmicpc.net/problem/14490
"""

s = input()
s1 = s.split(':')
a = int(s1[0])
b = int(s1[1])
k = 2
while 1:
    if a % k == 0 and b % k == 0:
        a //= k
        b //= k
        k = 2
    else:
        k += 1
    if k > a and k > b:
        break
print(f"{a}:{b}")
