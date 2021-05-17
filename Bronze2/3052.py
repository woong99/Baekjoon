# 나머지

"""
2021/05/17 4:21 오후
정웅교
문제: https://www.acmicpc.net/problem/3052
"""
ls = list()
sum = 0
for _ in range(10):
    ls.append(int(input()) % 42)
for i in range(42):
    if ls.count(i) >= 1:
        sum += 1
print(sum)
