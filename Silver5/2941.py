# 크로아티아 알파벳

"""
2021/06/25 8:21 오후
정웅교
문제: https://www.acmicpc.net/problem/2941
"""
s = input()
ls = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in ls:
    s = s.replace(i, '*')
print(len(s))
