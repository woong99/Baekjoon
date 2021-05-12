# 조교는 새디스트야!!

"""
2021/05/12 1:10 오후
정웅교
문제: https://www.acmicpc.net/problem/14656
"""
n = int(input())
ls = list(map(int, input().split()))
ls1 = list(ls)
ls.sort()
cnt = 0
for i in range(n):
    if ls[i] == ls1[i]:
        cnt += 1
print(n - cnt)
