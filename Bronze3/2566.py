# 최댓값

"""
2021/04/01 1:39 오후
정웅교
문제: https://www.acmicpc.net/problem/2566
"""

ls = []
for i in range(9):
    ls.append((list(map(int, input().split()))))
ls1 = []
for i in range(9):
    ls1.append(max(ls[i]))
print(max(ls1))
for i in range(9):
    for k in range(9):
        if ls[i][k] == max(ls1):
            print(i + 1, k + 1)
            break
