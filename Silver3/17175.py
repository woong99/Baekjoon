# 피보나치는 지겨웡~

"""
2021/08/16 1:19 오후
정웅교
문제: https://www.acmicpc.net/problem/17175
"""
n = int(input())
ls = [1, 1, 3]

for i in range(3, n + 1):
    ls.append((ls[i - 1] + ls[i - 2] + 1) % 1000000007)
print(ls[n])
