# Speed fines are not fine!

"""
2021/03/19 1:36 오후
정웅교
문제: https://www.acmicpc.net/problem/6763
"""
a = int(input())
b = int(input())
gap = b - a
if 1 <= gap <= 20:
    print('You are speeding and your fine is $100.')
elif 21 <= gap <= 30:
    print('You are speeding and your fine is $270.')
elif gap >= 31:
    print('You are speeding and your fine is $500.')
else:
    print('Congratulations, you are within the speed limit!')
