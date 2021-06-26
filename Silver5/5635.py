# 생일

"""
2021/06/27 1:34 오전
정웅교
문제: https://www.acmicpc.net/problem/5635
"""
ls = []
for _ in range(int(input())):
    ls.append(list(map(str, input().split())))
ls.sort(reverse=True, key=lambda x: (int(x[3]), int(x[2]), int(x[1])))

print(ls[0][0])
print(ls[len(ls) - 1][0])
