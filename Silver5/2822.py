# 점수 계산

"""
2021/06/21 6:17 오후
정웅교
문제: https://www.acmicpc.net/problem/2822
"""

dic = {}
for i in range(8):
    n = int(input())
    dic[i] = n
dic = sorted(dic.items(), key=lambda item: item[1])
dic1 = dic[3:8]
sum = 0
for i in range(5):
    sum += dic[i + 3][1]
print(sum)
dic1.sort()
for i in range(5):
    print(dic1[i][0] + 1, end=' ')
