# ROT13

"""
2021/06/01 3:46 오후
정웅교
문제: https://www.acmicpc.net/problem/11655
"""
s = input()
for i in s:
    if i.isdigit():
        print(i, end='')
    elif i == ' ':
        print(' ', end='')
    elif i.islower() == True and ord(i) + 13 > 122:
        print(chr(109 - (122 - ord(i))), end='')
    elif i.isupper() == True and ord(i) + 13 > 90:
        print(chr(ord(i) - 13), end='')
    else:
        print(chr(ord(i) + 13), end='')
