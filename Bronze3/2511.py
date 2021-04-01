# 카드놀이

"""
2021/04/01 1:12 오후
정웅교
문제: https://www.acmicpc.net/problem/2511
"""

A = list(map(int, input().split()))
B = list(map(int, input().split()))

if A == B:
    print(10, 10);
    print("D")
else:
    a = b = 0
    for i in range(10):
        if A[i] > B[i]:
            a += 3;
            win = 'A'
        elif A[i] < B[i]:
            b += 3;
            win = 'B'
        else:
            a += 1;
            b += 1;
    print(a, b)
    if a == b:
        print(win)
    else:
        print('A' if a > b else 'B')
