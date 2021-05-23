# 대소문자 바꾸기

"""
2021/05/23 2:49 오후
정웅교
문제: https://www.acmicpc.net/problem/2744
"""
s = str(input())
s1 = ''
for i in range(len(s)):
    if s[i].islower():
        s1 += (s[i].upper())
    elif s[i].isupper():
        s1 += (s[i].lower())
print(s1)
