# 팩토리얼

"""
2021/05/06 5:13 오후
정웅교
문제: https://www.acmicpc.net/problem/10872
"""
n = int(input())
res = 1;
for i in range(1, n + 1):
    res *= i
print(res)
