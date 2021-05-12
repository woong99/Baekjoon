# 우유 축제

"""
2021/05/12 1:16 오후
정웅교
문제: https://www.acmicpc.net/problem/14720
"""
n = int(input())
ls = list(map(int, input().split()))
st = -1
cnt = 0
for i in ls:
    if i == 0 and st == -1:
        st = 0
        cnt += 1
    elif i == 1 and st == 0:
        st = 1
        cnt += 1
    elif i == 2 and st == 1:
        st = -1
        cnt += 1
print(cnt)
