# 숫자 빈도수

"""
2021/06/23 8:21 오후
정웅교
문제: https://www.acmicpc.net/problem/14912
"""

a, b = map(int, input().split())
cnt = 0
for i in range(1, a + 1):
    cnt += str(i).count(str(b))
print(cnt)
