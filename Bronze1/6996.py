# 애너그램

"""
2021/06/11 3:05 오후
정웅교
문제: https://www.acmicpc.net/problem/6996
"""

for _ in range(int(input())):
    s1, s2 = map(str, input().split())
    a, b = list(s1), list(s2)
    a.sort()
    b.sort()
    if a == b:
        print(f"{s1} & {s2} are anagrams.")
    else:
        print(f"{s1} & {s2} are NOT anagrams.")
