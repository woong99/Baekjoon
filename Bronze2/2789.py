# 유학 금지

"""
2021/05/25 2:41 오후
정웅교
문제: https://www.acmicpc.net/problem/2789
"""
s = input()
a = 'CAMBRIDGE'
for i in a:
    s = s.replace(i, '')
print(s)
