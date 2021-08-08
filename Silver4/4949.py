# 균형잡힌 세상

"""
2021/08/08 2:47 오후
정웅교
문제: https://www.acmicpc.net/problem/4949
"""
while True:
    bracket = input()
    if bracket == ".":
        break
    bracket_stack = []
    answer = True

    for j in bracket:
        if j == "(" or j == "[":
            bracket_stack.append(j)

        elif j == ")":
            if len(bracket_stack) == 0:
                answer = False
                break
            if bracket_stack[-1] == "(":
                bracket_stack.pop()
            else:
                answer = False
                break

        elif j == "]":
            if len(bracket_stack) == 0:
                answer = False
                break
            if bracket_stack[-1] == "[":
                bracket_stack.pop()
            else:
                answer = False
                break

    if answer and not bracket_stack:
        print("yes")
    else:
        print("no")
