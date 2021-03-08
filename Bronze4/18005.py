# Even or Odd?

"""
2021/03/08 3:16 오후
정웅교
문제: https://www.acmicpc.net/problem/18005
"""

n = int(input())
if n % 2 == 1:
    print('0')
elif (n + 2) % 4 == 0:
    print('1')
else:
    print('2')
