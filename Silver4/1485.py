# 정사각형

"""
2021/08/08 3:19 오후
정웅교
문제: https://www.acmicpc.net/problem/1485
"""
for _ in range(int(input())):
    ls = []
    for _ in range(4):
        ls.append(list(map(int, input().split())))
    ls.sort()
    if abs(ls[3][0] - ls[0][0]) ** 2 + abs(ls[3][1] - ls[0][1]) ** 2 == abs(ls[2][0] - ls[1][0]) ** 2 + abs(
            ls[2][1] - ls[1][1]) ** 2:
        if (ls[1][0] - ls[0][0]) ** 2 + (ls[1][1] - ls[0][1]) ** 2 == (ls[2][0] - ls[0][0]) ** 2 + (
                ls[2][1] - ls[0][1]) ** 2:
            if (ls[2][0] - ls[0][0]) ** 2 + (ls[2][1] - ls[0][1]) ** 2 == (ls[3][0] - ls[1][0]) ** 2 + (
                    ls[3][1] - ls[1][1]) ** 2:
                if (ls[3][0] - ls[1][0]) ** 2 + (ls[3][1] - ls[1][1]) ** 2 == (ls[3][0] - ls[2][0]) ** 2 + (
                        ls[3][1] - ls[2][1]) ** 2:
                    print(1)
        else:
            print(0)
    else:
        print(0)
