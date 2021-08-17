# 대칭 차집합

"""
2021/08/17 10:49 오전
정웅교
문제: https://www.acmicpc.net/problem/1269
"""

a, b = map(int, input().split())
s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))
n1 = s1 - s2
n2 = s2 - s1
print(len(n1) + len(n2))
