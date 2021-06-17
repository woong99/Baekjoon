# 약수들의 합

"""
2021/06/17 4:35 오후
정웅교
문제: https://www.acmicpc.net/problem/9506
"""
while 1:
    n = int(input())
    if n == -1:
        break
    ls = [1]
    for i in range(2, n):
        if n % i == 0:
            ls.append(i)
    if sum(ls) == n:
        print(f"{n} = ", end='')
        for i in range(len(ls)):
            if i == len(ls) - 1:
                print(f"{ls[i]}")
            else:
                print(f"{ls[i]} + ", end='')
    else:
        print(f"{n} is NOT perfect.")
