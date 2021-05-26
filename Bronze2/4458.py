# 첫 글자를 대문자로

"""
2021/05/26 1:45 오후
정웅교
문제: https://www.acmicpc.net/problem/4458
"""

for _ in range(int(input())):
    s = str(input())
    if s[0].islower():
        s = s[0].upper() + s[1:]
    print(s)
