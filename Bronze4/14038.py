# Tournament Selection

"""
2021/03/19 1:46 오후
정웅교
문제: https://www.acmicpc.net/problem/14038
"""
a = input()
b = input()
c = input()
d = input()
e = input()
f = input()
sum = 0
ls = [a, b, c, d, e, f]
for i in range(6):
    if ls[i] == 'W':
        sum += 1

if sum == 5 or sum == 6:
    print('1')
elif sum == 3 or sum == 4:
    print('2')
elif sum == 1 or sum == 2:
    print('3')
else:
    print('-1')
