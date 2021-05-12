# 양수 개수 세기

"""
2021/05/12 1:03 오후
정웅교
문제: https://www.acmicpc.net/problem/14909
"""

ls = list(map(int, input().split()))
cnt = 0
for i in ls:
    if i > 0:
        cnt += 1
print(cnt)
