# 보물

"""
2021/07/11 3:36 오후
정웅교
문제: https://www.acmicpc.net/problem/1026
"""
n = int(input())
ls1 = list(map(int, input().split()))
ls2 = list(map(int, input().split()))
ls1.sort()
ls2.sort(reverse=True)
sum = 0
for i in range(n):
    sum += ls1[i] * ls2[i]
print(sum)
