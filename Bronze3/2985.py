# 세 수

"""
2021/04/05 9:36 오후
정웅교
문제: https://www.acmicpc.net/problem/2985
"""
a, b, c = map(int, input().split())
if a + b == c:
    print(f"{a}+{b}={c}")
elif a - b == c:
    print(f"{a}-{b}={c}")
elif a * b == c:
    print(f"{a}*{b}={c}")
else:
    print(f"{a}%{b}={c}")
