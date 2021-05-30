# 세로읽기

"""
2021/05/30 11:04 오전
정웅교
문제: https://www.acmicpc.net/problem/10798
"""
ls1 = input()
ls2 = input()
ls3 = input()
ls4 = input()
ls5 = input()
for i in range(max(len(ls1), len(ls2), len(ls3), len(ls4), len(ls5))):
    if i > len(ls1) - 1:
        pass
    else:
        print(ls1[i], end='')
    if i > len(ls2) - 1:
        pass
    else:
        print(ls2[i], end='')
    if i > len(ls3) - 1:
        pass
    else:
        print(ls3[i], end='')
    if i > len(ls4) - 1:
        pass
    else:
        print(ls4[i], end='')
    if i > len(ls5) - 1:
        pass
    else:
        print(ls5[i], end='')
