# 2007년

"""
2021/06/06 1:33 오후
정웅교
문제: https://www.acmicpc.net/problem/1924
"""
a, b = map(int, input().split())
sum = 0
for i in range(1, a):
    if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
        sum += 31
    elif i == 2:
        sum += 28
    else:
        sum += 30
sum += b
if sum % 7 == 1:
    print('MON')
elif sum % 7 == 2:
    print('TUE')
elif sum % 7 == 3:
    print('WED')
elif sum % 7 == 4:
    print('THU')
elif sum % 7 == 5:
    print('FRI')
elif sum % 7 == 6:
    print('SAT')
else:
    print('SUN')
