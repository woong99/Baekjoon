# 모음의 개수

"""
2021/05/23 1:09 오후
정웅교
문제: https://www.acmicpc.net/problem/10987
"""
s = str(input())
sum = 0
for i in s:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        sum += 1
print(sum)
