# 농구 경기

"""
2021/05/23 2:14 오후
정웅교
문제: https://www.acmicpc.net/problem/1159
"""
li = sorted([input()[0] for _ in range(int(input()))])
s = set(li)
res = []
for c in s:
    if li.count(c) >= 5:
        res.append(c)
print(''.join(sorted(res)) if len(res) > 0 else "PREDAJA")
