# 괄호

"""
2021/08/08 2:30 오후
정웅교
문제: https://www.acmicpc.net/problem/9012
"""
bre = True
for _ in range(int(input())):
    s = input()
    ls = []
    for i in s:
        if i == '(':
            ls.append(i)
        else:
            if len(ls) == 0:
                print('NO')
                bre = False
                break
            else:
                ls.pop()
    if bre:
        if len(ls) != 0:
            print('NO')
        else:
            print('YES')
    bre = True
