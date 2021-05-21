# 그릇

"""
2021/05/21 1:51 오후
정웅교
문제: https://www.acmicpc.net/problem/7567
"""

n = str(input())
sum = 0
for i in range(len(n)):
    if i == 0:
        sum += 10
    else:
        if n[i - 1] != n[i]:
            sum += 10
        else:
            sum += 5
print(sum)
