# 나는야 포켓몬 마스터 이다솜

"""
2021/08/07 11:05 오전
정웅교
문제: https://www.acmicpc.net/problem/1620
"""

a, b = map(int, input().split())
dic = {}
ls = []
for i in range(1, a + 1):
    s = input()
    ls.append(s)
    dic[s] = i
for _ in range(b):
    s = str(input())
    if s.isalpha():
        print(dic[s])
    else:
        print(ls[int(s) - 1])
