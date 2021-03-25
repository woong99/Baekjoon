# 핸드폰 요금

"""
2021/03/25 4:06 오후
정웅교
문제: https://www.acmicpc.net/problem/1267
"""
n = int(input())
s = list(map(int, input().split()))
sum1 = 0
sum2 = 0
for i in s:
    sum1 += (i // 30) * 10 + 10
    sum2 += (i // 60) * 15 + 15
if sum1 > sum2:
    print('M', sum2)
elif sum1 < sum2:
    print('Y', sum1)
else:
    print('Y M', sum1)
