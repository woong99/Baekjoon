# 접미사 배열

"""
2021/07/19 10:53 오전
정웅교
문제: https://www.acmicpc.net/problem/11656
"""
s = input()
ls = []
for i in range(len(s)):
    ls.append(s[i:])
ls.sort()
for i in ls:
    print(i)
