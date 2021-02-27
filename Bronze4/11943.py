# 파일 옮기기

"""
2021/02/27 10:50 오후
정웅교
문제: https://www.acmicpc.net/problem/11943
"""

a, b = map(int, input().split())
c, d = map(int, input().split())
print(min(a + d, b + c))
