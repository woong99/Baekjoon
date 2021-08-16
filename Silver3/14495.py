# 피보나치 비스무리한 수열

"""
2021/08/16 1:33 오후
정웅교
문제: https://www.acmicpc.net/problem/14495
"""
n = int(input())
ls = [1, 1, 1]
for i in range(3, n + 1):
    ls.append(ls[i - 1] + ls[i - 3])
print(ls[n - 1])
