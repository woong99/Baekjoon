# 평균은 넘겠지

"""
2021/05/28 1:49 오후
정웅교
문제: https://www.acmicpc.net/problem/4344
"""
for _ in range(int(input())):
    a = list(map(int, input().split()))
    ave = sum(a[1:]) / a[0]
    cnt = 0
    for i in range(1, len(a)):
        if a[i] > ave:
            cnt += 1

    print("{:.3f}%".format((cnt / a[0]) * 100))
