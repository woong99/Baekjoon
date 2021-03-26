# 생장점

"""
2021/03/26 7:08 오후
정웅교
문제: https://www.acmicpc.net/problem/1703
"""
ls1 = []
while 1:
    l = list(map(int, input().split()))
    if l[0] == 0:
        break
    sum = l[1] - l[2]
    for i in range(3, len(l)):
        if i % 2 == 1:
            sum = sum * l[i] - l[i + 1]
    ls1.append(sum)
for i in ls1:
    print(i)
