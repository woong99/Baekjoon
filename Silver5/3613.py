# Java vs C++

"""
2021/06/29 8:12 오후
정웅교
문제: https://www.acmicpc.net/problem/3613
"""


# java로 변환
def tojava(text):
    # 첫번째 or 마지막 문자가 _일때 __가 있을때
    if text[0] == "_" or text[-1] == "_" or "__" in text:
        return "Error!"

    ans = ""
    flag = False

    for i in text:
        # 대문자 일때
        if ord(i) >= 65 and ord(i) <= 90:
            return "Error!"

        if i == "_":
            flag = True
            continue

        if flag == True:
            ans += i.upper()
            flag = False
            continue

        ans += i

    return ans


# c++로 변환
def toc(text):
    # 첫 문자가 대문자 일때
    if ord(text[0]) >= 65 and ord(text[0]) <= 90:
        return "Error!"

    ans = ""

    for i in text:
        # 대문자 일때
        if ord(i) >= 65 and ord(i) <= 90:
            ans += "_" + i.lower()
        else:
            ans += i

    return ans


text = input()

if "_" in text:
    print(tojava(text))
else:
    print(toc(text))
