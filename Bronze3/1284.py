# 집 주소

"""
2021/03/26 5:12 오후
정웅교
문제: https://www.acmicpc.net/problem/1284
"""

while 1:
    n = input()
    if n == '0':
        break
    else:
        sum = 1
        for i in n:
            if i == '1':
                sum += 2
            elif i == '2':
                sum += 3
            elif i == '0':
                sum += 4
            else:
                sum += 3
            sum += 1
    print(sum)
