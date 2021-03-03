# 팀 나누기

"""
2021/03/03 10:24 오전
정웅교
문제: https://www.acmicpc.net/problem/13866
"""

a, b, c, d = map(int, input().split())

n1 = abs((a + b) - (c + d))
n2 = abs((a + c) - (b + d))
n3 = abs((a + d) - (b + c))
ls = [n1, n2, n3]
print(min(ls))
