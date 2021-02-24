# 조별과제를 하려는데 조장이 사라졌다

"""
2021/02/24 5:04 오후
정웅교
문제: https://www.acmicpc.net/problem/15727
"""

a = int(input())
if a % 5 == 0:
    print(a // 5)
else:
    print(a // 5 + 1)
