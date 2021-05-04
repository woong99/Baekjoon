# 사과

"""
2021/05/04 2:55 오후
정웅교
문제: https://www.acmicpc.net/problem/10833
"""

n = int(input())
rst = 0
for _ in range(n):
    a, b = map(int, input().split())
    rst += b - ((b // a) * a)
print(rst)
