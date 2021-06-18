# Doubles

"""
2021/06/19 3:48 오전
정웅교
문제: https://www.acmicpc.net/problem/4641
"""
while 1:
    ls = list(map(int, input().split()))
    if -1 in ls:
        break
    ls.remove(0)
    cnt = 0
    for i in ls:
        if i * 2 in ls:
            cnt += 1
    print(cnt)
