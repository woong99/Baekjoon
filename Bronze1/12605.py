# 단어순서 뒤집기

"""
2021/06/13 12:21 오후
정웅교
문제: https://www.acmicpc.net/problem/12605
"""
for i in range(int(input())):
    s = input()
    ls = s.split(' ')
    print(f"Case #{i + 1}: ", end='')
    for i in ls[::-1]:
        print(i, end=' ')
    print()
