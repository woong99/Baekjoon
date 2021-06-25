# 30

"""
2021/06/25 9:05 오후
정웅교
문제: https://www.acmicpc.net/problem/10610
"""
n = list(input())
n.sort(reverse=True)
sum = 0
for i in n:
    sum += int(i)
if sum % 3 == 0 and n[len(n) - 1] == '0':
    print(''.join(n))
else:
    print(-1)
