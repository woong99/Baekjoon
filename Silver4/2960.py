# 에라토스테네스의 체

"""
2021/08/09 11:35 오전
정웅교
문제: https://www.acmicpc.net/problem/2960
"""
stat = 2
cnt = 0
num = 0
num1 = 0
n, k = map(int, input().split())
ls = [i for i in range(2, n + 1)]
while cnt < k:
    if stat == 2:
        num = ls[0]
        num1 = ls[0]
        del (ls[0])
        cnt += 1
        stat = 3
    elif stat == 3:
        stat = 4
        for i in range(len(ls)):
            if ls[i] % num == 0:
                num1 = ls[i]
                del (ls[i])
                cnt += 1
                stat = 3
                break

    elif stat == 4 and len(ls) != 0:
        stat = 2
print(num1)
