# 8진수

"""
2021/06/19 12:57 오전
정웅교
문제: https://www.acmicpc.net/problem/2998
"""
n = input()
s = ''
if len(n) % 3 != 0:
    n = n.zfill((len(n) // 3 + 1) * 3)
for i in range(len(n) // 3):
    k = n[i * 3:i * 3 + 3]
    if k == '000':
        s += '0'
    elif k == '001':
        s += '1'
    elif k == '010':
        s += '2'
    elif k == '011':
        s += '3'
    elif k == '100':
        s += '4'
    elif k == '101':
        s += '5'
    elif k == '110':
        s += '6'
    else:
        s += '7'
print(s)
