# 일반 화학 실험

"""
2021/04/29 1:57 오후
정웅교
문제: https://www.acmicpc.net/problem/4766
"""

ls = []
i = 0
while 1:
    a = input()
    if a == '999':
        break
    i += 1
    ls.append(float(a))
    if i > 1:
        print(format(ls[i - 1] - ls[i - 2], ".2f"))
