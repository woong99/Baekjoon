# 공백 없는 A+B

"""
2021/03/02 5:51 오후
정웅교
문제: https://www.acmicpc.net/problem/15873
"""

n = input()
if len(n) == 2:
    print(int(n) % 10 + int(n) // 10)
elif len(n) == 3:
    if n[:2] == '10':
        print(int(n[:2]) + int(n[2]))
    else:
        print(int(n[0]) + int(n[1:]))
else:
    print(20)
