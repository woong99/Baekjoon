# 딱지놀이

"""
2021/06/19 12:22 오전
정웅교
문제: https://www.acmicpc.net/problem/14696
"""

for _ in range(int(input())):
    ls3 = [0, 0, 0, 0]
    ls4 = [0, 0, 0, 0]
    ls1 = list(map(int, input().split()))
    ls2 = list(map(int, input().split()))
    for i in range(1, len(ls1)):
        if ls1[i] == 1:
            ls3[3] += 1
        elif ls1[i] == 2:
            ls3[2] += 1
        elif ls1[i] == 3:
            ls3[1] += 1
        else:
            ls3[0] += 1
    for i in range(1, len(ls2)):
        if ls2[i] == 1:
            ls4[3] += 1
        elif ls2[i] == 2:
            ls4[2] += 1
        elif ls2[i] == 3:
            ls4[1] += 1
        else:
            ls4[0] += 1
    if ls3[0] > ls4[0]:
        print('A')
    elif ls3[0] < ls4[0]:
        print('B')
    elif ls3[0] == ls4[0] and ls3[1] > ls4[1]:
        print('A')
    elif ls3[0] == ls4[0] and ls3[1] < ls4[1]:
        print('B')
    elif ls3[0] == ls4[0] and ls3[1] == ls4[1] and ls3[2] < ls4[2]:
        print('B')
    elif ls3[0] == ls4[0] and ls3[1] == ls4[1] and ls3[2] > ls4[2]:
        print('A')
    elif ls3[0] == ls4[0] and ls3[1] == ls4[1] and ls3[2] == ls4[2] and ls3[3] < ls4[3]:
        print('B')
    elif ls3[0] == ls4[0] and ls3[1] == ls4[1] and ls3[2] == ls4[2] and ls3[3] > ls4[3]:
        print('A')
    else:
        print('D')
