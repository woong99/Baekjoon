# 알람 시계

"""
2021/04/04 2:49 오후
정웅교
문제: https://www.acmicpc.net/problem/2884
"""

h, m = map(int, input().split())
sum = h * 60 + m
if (sum - 45) // 60 < 0:
    print(24 + ((sum - 45) // 60), (sum - 45) % 60)
else:
    print((sum - 45) // 60, (sum - 45) % 60)
