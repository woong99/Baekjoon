# 소트인사이드

"""
2021/06/20 12:18 오전
정웅교
문제: https://www.acmicpc.net/problem/1427
"""
s = list(input())
s.sort()
s.reverse()
for i in s:
    print(i, end='')
