# 폴리오미노

"""
2021/06/26 12:13 오전
정웅교
문제: https://www.acmicpc.net/problem/1343
"""
s = input()
s = s.replace('XXXX', 'AAAA')
s = s.replace('XX', 'BB')
if 'X' in s:
    print(-1)
else:
    print(s)
