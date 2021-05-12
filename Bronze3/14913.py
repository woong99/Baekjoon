# 등차수열에서 항 번호 찾기

"""
2021/05/12 1:24 오후
정웅교
문제: https://www.acmicpc.net/problem/14913
"""
a, d, k = map(int, input().split())
print((k - a) // d + 1 if (k - a) % d == 0 and (k - a) // d >= 0 else 'X')
