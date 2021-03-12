# Every Second Counts

"""
2021/03/12 1:01 오후
정웅교
문제: https://www.acmicpc.net/problem/15080
"""
a = input()
b = input()
ls1 = a.split(':')
ls2 = b.split(':')
sum1 = int(ls1[0]) * 3600 + int(ls1[1]) * 60 + int(ls1[2])
sum2 = int(ls2[0]) * 3600 + int(ls2[1]) * 60 + int(ls2[2])
if sum1 > sum2:
    print(24 * 3600 - sum1 + sum2)
else:
    print(sum2 - sum1)
