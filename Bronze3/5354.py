# J박

"""
2021/05/01 10:45 오후
정웅교
문제: https://www.acmicpc.net/problem/5354
"""

n = int(input())
for _ in range(n):
    i = int(input())
    if i == 1:
        print('#' + '\n')
    else:
        print('#' * i)
        for t in range(i - 2):
            print('#' + 'J' * (i - 2) + '#')
        print('#' * i + '\n')
