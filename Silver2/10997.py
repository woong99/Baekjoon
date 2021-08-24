# 별 찍기 - 22

"""
2021/08/24 7:42 오후
정웅교
문제: https://www.acmicpc.net/problem/10997
"""
n = int(input())
if n == 1:
    print('*')
    exit()
print('*' * (4 * n - 3))
print('*')
for i in range(1, n):
    print('* ' * i + '*' * (-4 * i + 4 * n - 1) + ' *' * (i - 1))
    if i != n - 1:
        print('* ' * (i + 1) + ' ' * (-4 * i + 4 * n - 5) + ' *' * i)
print('* ' * (2 * n - 1))
print('* ' * (2 * n - 1))
for i in range(1, n - 1):
    print('* ' * (-i + n) + ' ' * (4 * i - 3) + ' *' * (n - i))
    print('* ' * (n - i - 1) + '*' * (4 * i + 1) + ' *' * (n - i - 1))
print('*' + ' ' * (4 * n - 5) + '*')
print('*' * (4 * n - 3))
