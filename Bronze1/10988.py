# 팰린드롬인지 확인하기

"""
2021/05/30 10:57 오전
정웅교
문제: https://www.acmicpc.net/problem/10988
"""
s = input()
a = ''
a += s[::-1]
if a == s:
    print(1)
else:
    print(0)
