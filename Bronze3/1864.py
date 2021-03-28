# 문어 숫자

"""
2021/03/28 12:01 오후
정웅교
문제: https://www.acmicpc.net/problem/1864
"""
ls = ['-', '\\', '(', '@', '?', '>', '&', '%', '/']
while 1:
    n = input()
    ls1 = []
    if n == '#':
        break
    for i in n:
        for k in ls:
            if i == k:
                if i == '/':
                    ls1.append(-1)
                else:
                    ls1.append(ls.index(k))
    ls1.reverse()
    sum = 0
    n = 0
    for i in ls1:
        sum += i * (8 ** n)
        n += 1
    print(sum)
