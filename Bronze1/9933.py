# 민균이의 비밀번호

"""
2021/06/07 4:34 오후
정웅교
문제: https://www.acmicpc.net/problem/9933
"""
ls1 = []
ls2 = []
for _ in range(int(input())):
    s = input()
    ls1.append(s)
    ls2.append(s[::-1])
k = list(set(ls1) & set(ls2))
s = str(k[0])
print(len(s), s[len(s) // 2])
