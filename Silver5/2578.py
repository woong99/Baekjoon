# 빙고

"""
2021/06/27 12:40 오전
정웅교
문제: https://www.acmicpc.net/problem/2578
"""


def isCheck(check):
    cnt = 0
    # 가로
    for i in range(5):
        flag = True
        if False in check[i]:
            flag = False
        if flag:
            cnt += 1
    # 세로
    col_check = list(map(list, zip(*check)))
    for i in range(5):
        flag = True
        if False in col_check[i]:
            flag = False
        if flag:
            cnt += 1

    # 대각선
    r_flag, l_flag = True, True
    for i in range(5):
        if check[i][i] == 0:
            r_flag = False
        if check[i][4 - i] == 0:
            l_flag = False
    if r_flag:
        cnt += 1
    if l_flag:
        cnt += 1

    if cnt >= 3:
        return True
    return False


if __name__ == '__main__':
    arr = []
    mc = []
    ch = [[False] * 5 for _ in range(5)]
    count = 0

    for i in range(5):
        arr.append(list(map(int, input().split())))
    for i in range(5):
        mc.append(list(map(int, input().split())))

    for x in mc:
        while x:
            num = x.pop(0)
            count += 1
            for i in range(5):
                for j in range(5):
                    if arr[i][j] == num:
                        ch[i][j] = True
                        break

            if count >= 5 and isCheck(ch):
                print(count)
                exit()
