# 카이사르 암호

"""
2021/05/24 3:26 오후
정웅교
문제: https://www.acmicpc.net/problem/5598
"""

s = input()
for i in s:
    if 65 <= ord(i) <= 67:
        a = ord(i) + 23
    else:
        a = ord(i) - 3
    print(chr(a), end='')
print()
