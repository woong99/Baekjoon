# 가위 바위 보?

"""
2021/04/28 2:31 오후
정웅교
문제: https://www.acmicpc.net/problem/4493
"""

n = int(input())
for _ in range(n):
    k = int(input())
    cnta = 0
    cntb = 0
    for i in range(k):
        a, b = map(str, input().split())
        if a == 'R' and b == 'P':
            cntb += 1
        elif a == 'R' and b == 'S':
            cnta += 1
        elif a == 'P' and b == 'R':
            cnta += 1
        elif a == 'P' and b == 'S':
            cntb += 1
        elif a == 'S' and b == 'R':
            cntb += 1
        elif a == 'S' and b == 'P':
            cnta += 1
    if cnta > cntb:
        print('Player 1')
    elif cnta < cntb:
        print('Player 2')
    else:
        print('TIE')
