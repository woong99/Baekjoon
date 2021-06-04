# 나머지와 몫이 같은 수

"""
2021/06/04 1:27 오후
정웅교
문제: https://www.acmicpc.net/problem/1834
"""
n = int(input())
sum = 0
i = 1
while 1:
    if i % n == i // n:
        sum += i
        i = i + n
    else:
        i += 1
    if i // n >= n:
        break
print(sum)
