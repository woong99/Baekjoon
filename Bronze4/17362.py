# 수학은 체육과목 입니다 2

"""
2021/02/28 5:54 오후
정웅교
문제: https://www.acmicpc.net/problem/17362
"""

n = int(input())
if (n - 1) % 8 == 0:
    print(1)
elif (n - 3) % 4 == 0:
    print(3)
elif (n - 5) % 8 == 0:
    print(5)
elif (n - 2) % 8 == 0 or n % 8 == 0:
    print(2)
else:
    print(4)
