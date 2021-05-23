# 5와 6의 차이

"""
2021/05/23 1:29 오후
정웅교
문제: https://www.acmicpc.net/problem/2864
"""
a, b = map(str, input().split())
s1 = ''
s2 = ''
s3 = ''
s4 = ''
for i in a:
    if i == '5':
        s1 += '6'
    else:
        s1 += i
for i in b:
    if i == '5':
        s2 += '6'
    else:
        s2 += i
for i in a:
    if i == '6':
        s3 += '5'
    else:
        s3 += i
for i in b:
    if i == '6':
        s4 += '5'
    else:
        s4 += i
print(int(s3) + int(s4), int(s1) + int(s2))
