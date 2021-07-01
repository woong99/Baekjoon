# 한윤정이 이탈리아에 가서 아이스크림을 사먹는데

"""
2021/06/30 11:33 오후
정웅교
문제: https://www.acmicpc.net/problem/2422
"""

N, M = map(int, input().split())
cnt = 0
if N < 3:
    print(cnt)
else:
    unmixed = {i: [] for i in range(1, N + 1)}
    for _ in range(M):
        i, j = map(int, input().split())
        unmixed[i].append(j)
        unmixed[j].append(i)

    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            if j in unmixed[i]:
                continue
            for k in range(j + 1, N + 1):
                if k in unmixed[i] or k in unmixed[j]:
                    continue
                cnt += 1
    print(cnt)
