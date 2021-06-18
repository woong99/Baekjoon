# 謎紛芥索紀 (Small)

"""
2021/06/19 4:52 오전
정웅교
문제: https://www.acmicpc.net/problem/14730
"""
sum = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    sum += a * b
print(sum)
