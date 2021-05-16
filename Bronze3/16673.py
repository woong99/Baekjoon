# 고려대학교에는 공식 와인이 있다

"""
2021/05/17 12:39 오전
정웅교
문제: https://www.acmicpc.net/problem/16673
"""

c, k, p = map(int, input().split())
sum = 0
for i in range(1, c + 1):
    sum += i * k + i ** 2 * p
print(sum)
