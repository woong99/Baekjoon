# Hard choice

"""
2021/03/09 5:26 오후
정웅교
문제: https://www.acmicpc.net/problem/15059
"""
a, b, c = map(int, input().split())
d, e, f = map(int, input().split())
sum = 0
if d > a:
    sum += d - a
if e > b:
    sum += e - b
if f > c:
    sum += f - c
print(sum)
