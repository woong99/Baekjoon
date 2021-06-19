# 단어 정렬

"""
2021/06/20 12:23 오전
정웅교
문제: https://www.acmicpc.net/problem/1181
"""
n = int(input())
ls = []
for _ in range(n):
    ls.append(input())
ls = list(set(ls))
ls.sort(key=lambda x: (len(x), x))
print("\n".join(ls))
