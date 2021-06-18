# 단어 퍼즐

"""
2021/06/19 4:55 오전
정웅교
문제: https://www.acmicpc.net/problem/9946
"""
i = 1
while 1:
    s1 = input()
    s2 = input()
    if s1 == s2 == 'END':
        break
    s1 = sorted(list(s1))
    s2 = sorted(list(s2))
    if s1 == s2:
        print(f"Case {i}: same")
    else:
        print(f"Case {i}: different")
    i += 1
