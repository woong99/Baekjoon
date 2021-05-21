# 2진수 8진수

"""
2021/05/21 1:37 오후
정웅교
문제: https://www.acmicpc.net/problem/1373
"""

n = str(input())
n1 = n.split()
n1.insert(0, '0b')
n = ''.join(n1)
a = int(n, 2)
print(format(a, 'o'))
