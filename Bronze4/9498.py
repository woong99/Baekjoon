# 시험 성적

"""
2021/02/25 9:43 오후
정웅교
문제: https://www.acmicpc.net/problem/9498
"""

n = int(input())
if 90 <= n <= 100:
    print('A')
elif 80 <= n < 90:
    print('B')
elif 70 <= n < 80:
    print('C')
elif 60 <= n < 70:
    print('D')
else:
    print('F')
