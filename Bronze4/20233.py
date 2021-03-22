# Bicycle

"""
2021/03/22 2:05 오후
정웅교
문제: https://www.acmicpc.net/problem/20233
"""
a = int(input())
x = int(input())
b = int(input())
y = int(input())
T = int(input())
A = a + max(T - 30, 0) * x * 21
B = b + max(T - 45, 0) * y * 21
print(A, B)
