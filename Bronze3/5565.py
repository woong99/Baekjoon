# 영수증

"""
2021/05/02 2:11 오후
정웅교
문제: https://www.acmicpc.net/problem/5565
"""

n = int(input())
result = 0
for _ in range(9):
    k = int(input())
    result += k
print(n - result)
