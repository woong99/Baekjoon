# 숫자세는 양 (Large)

"""
2021/07/01 8:15 오전
정웅교
문제: https://www.acmicpc.net/problem/14382
"""

for p in range(int(input())):
    n = input()
    if n == '0':
        print(f"Case #{p + 1}: INSOMNIA")
    else:
        s1 = set()
        s = set(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'))
        n1 = n
        i = 1
        while 1:
            for k in str(int(n) * i):
                s1.add(k)
            if s1 == s:
                break
            i += 1
        print(f"Case #{p + 1}: {int(n) * i}")
