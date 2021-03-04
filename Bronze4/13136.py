# Do Not Touch Anything

"""
2021/03/04 10:33 오전
정웅교
문제: https://www.acmicpc.net/problem/13136
"""

r, c, n = map(int, input().split())
if r % n == 0:
    a = r // n
else:
    a = r // n + 1
if c % n == 0:
    b = c // n
else:
    b = c // n + 1
print(a * b)
