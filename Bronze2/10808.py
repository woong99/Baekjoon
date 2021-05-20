# 알파벳 개수

"""
2021/05/20 1:26 오후
정웅교
문제: https://www.acmicpc.net/problem/10808
"""

s = str(input())
ls = [0 for i in range(26)]
for i in s:
    ls[ord(i) - 97] += 1
for i in ls:
    print(i, end=' ')
