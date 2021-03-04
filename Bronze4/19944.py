# 뉴비의 기준은 뭘까?

"""
2021/03/04 2:32 오후
정웅교
문제: https://www.acmicpc.net/problem/19944
"""

n, m = map(int, input().split())
if m <= 2:
    print('NEWBIE!')
elif 2 < m <= n:
    print('OLDBIE!')
else:
    print('TLE!')
