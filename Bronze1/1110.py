# 더하기 싸이클

"""
2021/05/28 12:00 오후
정웅교
문제: https://www.acmicpc.net/problem/1110
"""
n = input()
a = n
sum = 0
cnt = 0
num = ''
if n == '0':
    print(1)

else:
    if 0 < int(n) < 10:
        a = '0' + n
        n = '0' + n
    while 1:
        sum = int(a[0]) + int(a[1])
        sum = str(sum)
        num = a[1] + sum[len(sum) - 1]
        a = num
        cnt += 1
        if a == n:
            break

    print(cnt)
