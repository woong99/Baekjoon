# 등수 구하기

"""
2021/06/28 3:36 오전
정웅교
문제: https://www.acmicpc.net/problem/1205
"""

import sys

n, yj, p = input().split()
nums = list(map(int, sys.stdin.readline().split()))
over = 0

if int(p) == 0:  # 랭킹 길이가 0이면 -1반환
    print(-1)
elif int(n) == 0:  # 입력 점수가 0개면 1등반환
    print(1)
else:
    nums.append(int(yj))  # yj의 점수 추가
    nums.sort(reverse=True)  # 정렬
    if nums.index(int(yj)) + 1 > int(p):  # yj의 등수가 랭킹 범위를 넘으면
        print(-1)  # -1반환
    else:
        if int(yj) == nums[-1] and int(n) == int(p):  # yj점수==마지막점수 AND n==p
            print(-1)  # -1 반환
        else:
            print(nums.index(int(yj)) + 1)
