# 오각형, 오각형, 오각형…

"""
2021/03/29 2:16 오후
정웅교
문제: https://www.acmicpc.net/problem/1964
"""

n = int(input())
i = 0
dot = 5
while i < n - 1:
    dot += 7 + 3 * i
    i += 1
print(dot % 45678)
