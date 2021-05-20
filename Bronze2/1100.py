# 하얀 칸

"""
2021/05/20 1:52 오후
정웅교
문제: https://www.acmicpc.net/problem/1100
"""
ls = []
for _ in range(8):
    ls.append((input()))
sum = 0
for i in range(8):
    if i % 2 == 0:
        for k in range(0, 8, 2):
            if ls[i][k] == 'F':
                sum += 1
    else:
        for k in range(1, 8, 2):
            if ls[i][k] == 'F':
                sum += 1
print(sum)
