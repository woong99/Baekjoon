# 그룹 단어 체커

"""
2021/06/20 12:09 오전
정웅교
문제: https://www.acmicpc.net/problem/1316
"""
n = 0
for _ in range(int(input())):
    s = input()
    ls = []
    cnt = 0
    for i in range(len(s)):
        if s[i] in ls:
            cnt += 1
        if i != len(s) - 1:
            if s[i] != s[i + 1]:
                ls.append(s[i])
    if cnt == 0:
        n += 1
print(n)
