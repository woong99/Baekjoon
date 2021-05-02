# 계산기 프로그램

"""
2021/05/02 11:26 오전
정웅교
문제: https://www.acmicpc.net/problem/5613
"""
ls = []
while 1:
    n = input()
    if n == "=":
        break

    ls.append(n)

result = int(ls[0])
for i in range(len(ls)):
    if ls[i] == "+":
        result += int(ls[i + 1])
    elif ls[i] == '*':
        result *= int(ls[i + 1])
    elif ls[i] == '/':
        result = result // int(ls[i + 1])
    elif ls[i] == '-':
        result -= int(ls[i + 1])
print(result)
