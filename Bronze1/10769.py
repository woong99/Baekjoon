# 행복한지 슬픈지

"""
2021/06/14 3:31 오후
정웅교
문제: https://www.acmicpc.net/problem/10769
"""
s = input()
cnt1, cnt2 = 0, 0
for i in range(len(s)):
    if s[i] == ':':
        if s[i + 1] == '-' and s[i + 2] == ')':
            cnt1 += 1
        elif s[i + 1] == '-' and s[i + 2] == '(':
            cnt2 += 1
if cnt1 == 0 and cnt2 == 0:
    print('none')
elif cnt1 > cnt2:
    print('happy')
elif cnt1 < cnt2:
    print('sad')
else:
    print('unsure')
