# 문서 검색

"""
2021/08/06 12:46 오후
정웅교
문제: https://www.acmicpc.net/problem/1543
"""

s1 = input()
s2 = input()
k = 0
cnt = 0
while k <= len(s1) - len(s2):
    if s1[k:k + len(s2)] == s2:
        cnt += 1
        k += len(s2)
    else:
        k += 1
print(cnt)
