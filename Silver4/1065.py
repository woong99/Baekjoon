# 한 수

"""
2021/07/11 3:24 오후
정웅교
문제: https://www.acmicpc.net/problem/1065
"""
n = input()
cnt = 0
for i in range(1, int(n) + 1):
    if len(str(i)) == 1 or len(str(i)) == 2:
        cnt += 1
    else:
        if int(str(i)[1]) - int(str(i)[0]) == int(str(i)[2]) - int(str(i)[1]):
            cnt += 1

print(cnt)
